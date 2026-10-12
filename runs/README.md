# Как запускались агенты

Путь к временной папке прогона заменён на `<папка прогона>`. В каждой папке перед запуском лежали ровно эти файлы:

| Прогон | Файлы в папке |
|---|---|
| `gen` — ящик и чат по ключу | `legend.json`, `prompt.md` |
| `v1-own-*`, `v2-own-*`, `v3-own-*` — план по нашим данным | `INSTRUCTION.md` (версии v1, v2, v3), `inbox.md`, `chat.md`, `prompt.txt` |

## Команды

Данные (одна сессия, `runs/gen/`):

```bash
cd <папка прогона>   # legend.json, prompt.md
claude -p --model claude-sonnet-5-5 --effort high --allowedTools "Read,Write,Edit" \
  --permission-mode acceptEdits "$(cat prompt.md)" </dev/null > answer.txt
```

План (Sonnet и Luna параллельно, каждый в своей папке; так для каждой версии инструкции):

```bash
cd <папка прогона>   # INSTRUCTION.md, inbox.md, chat.md, prompt.txt
claude -p --model claude-sonnet-5-5 --effort high --allowedTools "Read" \
  --output-format stream-json --verbose "$(cat prompt.txt)" </dev/null > transcript.jsonl

cd <папка прогона>   # INSTRUCTION.md, inbox.md, chat.md, prompt.txt
codex exec -m gpt-6-luna -c model_reasoning_effort=high --skip-git-repo-check -s read-only \
  -C <папка прогона> -o plan.md --json "$(cat prompt.txt)" </dev/null > transcript.jsonl
```

`plan.md` у Sonnet — поле `result` из `transcript.jsonl`, у Luna — файл `-o plan.md`. Оба скопированы без правок. В каждой папке:
- `prompt.txt` — промпт как есть. Его первая строка `Reason:` нужна обёртке запуска на нашей машине, которая записывает, почему выбрана модель.
- `tools.txt` — вызовы инструментов, выписанные из транскрипта.
- `transcript.jsonl` — транскрипт, из которого убрана строка с настройками машины (`system/init`), а путь к папке заменён.

Каждая версия запущена один раз на модель, перезапусков внутри версии не было.
