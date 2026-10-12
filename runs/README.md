# Как запускались агенты

Пути к временным папкам заменены на `<папка прогона>`. В каждой папке прогона перед запуском лежали ровно эти файлы:

| Прогон | Файлы в папке |
|---|---|
| `gen` — ящик и чат по ключу | `legend.json`, `prompt.md` |
| `own-sonnet`, `own-luna` — план по нашим данным | `INSTRUCTION.md`, `inbox.md`, `chat.md`, `prompt.txt` |

## Команды

Данные (одна сессия, `runs/gen/`):

```bash
cd <папка прогона>   # legend.json, prompt.md
claude -p --model claude-sonnet-5-5 --effort high --allowedTools "Read,Write,Edit" \
  --permission-mode acceptEdits "$(cat prompt.md)" </dev/null > answer.txt
```

План (два прогона параллельно, каждый в своей папке):

```bash
cd <папка прогона>   # INSTRUCTION.md, inbox.md, chat.md, prompt.txt
claude -p --model claude-sonnet-5-5 --effort high --allowedTools "Read" \
  --output-format stream-json --verbose "$(cat prompt.txt)" </dev/null > transcript.jsonl

cd <папка прогона>   # INSTRUCTION.md, inbox.md, chat.md, prompt.txt
codex exec -m gpt-6-luna -c model_reasoning_effort=high --skip-git-repo-check -s read-only \
  -C <папка прогона> -o plan.md --json "$(cat prompt.txt)" </dev/null > transcript.jsonl
```

`plan.md` у Sonnet — поле `result` из `transcript.jsonl`, у Luna — файл `-o plan.md`. Оба скопированы в репозиторий без правок. Полные транскрипты не выложены, потому что в них служебные данные машины. Из них выписаны вызовы инструментов — `tools.txt` в каждой папке. Оба прогона запущены один раз, перезапусков не было.
