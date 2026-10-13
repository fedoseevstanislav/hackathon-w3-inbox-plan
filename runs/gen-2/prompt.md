Reason: first attempt — claude-sonnet-5-5 high for generating stage-2 synthetic Russian sent emails and notes from a fixed legend (bounded content generation, checked by script afterwards).

Your folder contains a hackathon exercise («вернулись из отпуска → план на первый день») that already has its data: inbox.md (40 emails) and chat.md (80 messages) of the fictional web studio «Полоса», plus legend.json (the stage-1 answer key) and legend-2.json (the stage-2 answer key). Stage 2 adds Anya's sent emails and her notes. Do NOT change inbox.md, chat.md or the legends. Write three new files in this folder.

1. sent.md — exactly the 10 emails S01…S10 described in legend-2.json "sent", in that order, dates as given, strictly increasing time (working hours).
   First lines exactly:
   ```
   # Отправленные anya@polosa.studio — 21.09.2026–25.09.2026

   Письма, которые Аня Ковалёва отправила до отпуска.
   ```
   Each email exactly in the inbox.md format, with anchor and heading:
   ```
   <a id="s03"></a>
   ## S03 · 23.09.2026 14:20

   **От:** Аня Ковалёва <anya@polosa.studio>  
   **Кому:** Тимур Ахмедов <timur@mirknig-shop.ru>  
   **Тема:** Re: Новая корзина

   Текст письма.

   > цитата письма, на которое Аня отвечает (если это ответ)
   ```
   (Two trailing spaces after header lines are intended; «Копия» line only when there is a copy.) Anya's voice: short, friendly, businesslike, signed «Аня». Where she replies, quote the original below her text with «> ».

2. notes.md — the 4 notes N01…N04 from legend-2.json "notes".
   First lines exactly: `# Заметки Ани Ковалёвой — 22.09.2026–25.09.2026`, then an empty line.
   Each note:
   ```
   <a id="n02"></a>
   ## N02 · 25.09.2026

   Текст заметки — как человек пишет себе: коротко, обрывками.
   ```

3. map-2.json — {"sent": {"S01": "<one line: what the email says and which promise or non-promise it holds>", ...}, "notes": {"N01": "...", ...}, "checks": "<one paragraph: what you verified>"}.

Rules:
- Realise every sent email and note exactly as legend-2.json describes: recipient, date, the promise wording (keep the quoted phrases close to the legend: «да, беру», «гляну на неделе», «пришлю цифры по конверсии после релиза», «до нашей установочной встречи», «сразу после отпуска», «как только Рустам соберёт часы», «пришлю завтра»), and where the legend says there is NO date, write no date, no weekday and no relative deadline in that email. Never write legend ids (И1, О3, Л7, К1, …) or words like «легенда», «ключ», «ловушка», «обещание».
- S01 quotes Игорь's request with «хорошо бы до конца октября»; Anya's own text names no date.
- S03 and S04: no release date and no meeting date in the email. The release date (вт 29.09) appears only in note N01.
- N02 says, in Anya's words, that with the contractor everything is closed and nothing is owed — it must be clearly about Кира Белова and the illustrations for «Мир книг». Do not mention any invoice or sum there.
- S09 is a clear refusal; S10 is an out-of-office notice with no promise.
- Everything must agree with inbox.md and chat.md (people, roles, addresses, projects). Read both first. No new tasks for Anya beyond the legend; no other promises in any email (do not add «вернусь с ответом», «посмотрю», etc. where the legend has none).
- Addresses: use those in legend.json; Ксения Миронова <ksenia@zerno-coffee.ru> appears only in N03.

After writing, re-read the files and check numbering, dates, order, that each email holds exactly the promise or non-promise the legend gives, and that S01, S03, S04, S05, S06 contain no concrete date or weekday in Anya's own text. Fix any mismatch. Reply with one line: the counts.
