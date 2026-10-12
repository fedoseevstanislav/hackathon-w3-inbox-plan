Reason: first attempt — claude-sonnet-5-5 high for generating a synthetic Russian inbox and chat from a fixed legend (bounded content generation, checked by script afterwards).

Your folder contains legend.json: the hidden answer key for a hackathon exercise («вернулись из отпуска → план на первый день»). Write a synthetic mailbox and work chat of the fictional web studio «Полоса» that realise exactly this legend. Everything is fictional; use only the people, companies and addresses from the legend (plus invented service senders for noise). Write three files in this folder.

1. inbox.md — 40 emails, E01…E40 without gaps, strictly increasing time, from 26.09.2026 to 11.10.2026.
   First lines exactly:
   ```
   # Ящик anya@polosa.studio — 26.09.2026–11.10.2026

   Владелец: Аня Ковалёва, руководитель проектов, веб-студия «Полоса». Отпуск: 28.09.2026–09.10.2026. Первый рабочий день: пн 12.10.2026.
   ```
   Each email exactly like this (anchor line, heading, header lines, empty line, body, empty line):
   ```
   <a id="e07"></a>
   ## E07 · 07.10.2026 10:12

   **От:** Игорь Лебедев <igor@polosa.studio>  
   **Кому:** anya@polosa.studio  
   **Копия:** denis@polosa.studio  
   **Тема:** КП для Терра-Строй

   Текст письма.
   ```
   (Копия line only when there is a copy; the two trailing spaces after header lines are intended.) Bodies are realistic: greetings, signatures, quoted earlier text in replies («> …»), some long, some two lines. Noise emails look like real newsletters and service notifications: noreply addresses, «Отписаться» links, template text. About 18–20 of the 40 emails are noise per the legend; the rest realise the items, plus you may add 1–3 harmless personal or FYI emails with nothing for Anya to do (they are not plan items).

2. chat.md — 80 messages, C001…C080 without gaps, strictly increasing time, from 28.09.2026 to 11.10.2026, the last one on 09.10–11.10.
   First lines exactly: `# Чат «Полоса · команда» — 28.09.2026–11.10.2026`, then an empty line.
   Each message is one line, followed by an empty line:
   `<a id="c031"></a>[C031] 07.10.2026 09:12 · Денис: текст`
   A reply adds ` (в ответ на [C028])` at the end. Only Игорь, Денис, Оля, Рустам, Света speak, by first name; Аня never writes (she is on vacation). Most messages are NOT about the legend items: work chatter, lunch, jokes, deploys, bugs, typos, short replies («ок», «+»).

3. map.json — where each legend item and the noise sit:
   {"items": {"И1": {"emails": ["E.."], "chat": ["C.."], "closing": "C.." or null}, ...}, "noise": ["E..", ...], "personal": ["E..", ...]}
   "closing" is the message that closed a «решилось без вас» item; null for others. "personal" lists any harmless FYI emails you added (may be empty).

Rules:
- Realise every item, date, sum, time, name and trap of the legend exactly as stated (dates of emails and chat messages as given). Phrase everything naturally in different words; never write legend ids (И1, Л1, …) or words like «легенда», «ключ», «ловушка».
- Relative deadlines (И6, И12) must appear only as the relative phrase «к концу следующей недели» in the email, never as a concrete date anywhere in inbox or chat. The send dates of those emails must be exactly as in the legend (ср 07.10 and ср 30.09).
- И5: the three emails from Павел carry the three dates; the last one states 15.10 11:00. One calendar auto-reminder (noise) mentions the meeting at its OLD date 13.10 10:00 (trap Л6).
- И9: Тимур's two emails are alarming («СРОЧНО» in the subject), and the only closure is Денис's chat message 01.10 in the evening; no further email from Тимур about payment.
- И8 (HR) is written by a person (Карина) personally to Anya, though it looks like a mass mail at first glance.
- The monitoring alerts (Л4) are noreply, with «СРОЧНО» in the subject.
- Don't make extra items that need Anya's action beyond the legend's 14; the chat chatter must not create new tasks for Anya.

After writing, re-read the files and check: numbering, counts (40 and 80), increasing times, every map id points to an email or message that really says that, no concrete date for the two relative deadlines. Fix any mismatch. Reply with one line: the counts.
