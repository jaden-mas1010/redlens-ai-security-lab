# RedLens AI — Screenshot Evidence Index

This pack contains **14 screenshots shared in the ChatGPT project walkthrough**. The PNG files are copied without cropping, retouching, or modifying their contents. File names reflect the experiment, and the numbers broadly match the milestone labels used in the lessons.

**Important:** These are screenshots from a local test using the deliberately fictional identifier `RL-TEST-4821`. A model disclosing that value is an observed failure to follow a system instruction in this lab, not evidence of a real-world credential compromise. Different runs produced different responses. Do not claim this establishes a general attack-success probability.

## Captured evidence

| Screenshot | What it documents |
| --- | --- |
| [screenshots/02-python-chatbot.png](screenshots/02-python-chatbot.png) | First working Python chatbot connected to Ollama. |
| [screenshots/03-conversation-memory.png](screenshots/03-conversation-memory.png) | Chatbot remembers the user's stated favourite colour. |
| [screenshots/04-baseline-refusal.png](screenshots/04-baseline-refusal.png) | Normal request to reveal fictional code was refused. |
| [screenshots/05-authority-spoofing-manual.png](screenshots/05-authority-spoofing-manual.png) | First manual developer-impersonation attempt; no code disclosed. |
| [screenshots/06-multiturn-attack-manual.png](screenshots/06-multiturn-attack-manual.png) | Follow-up request; unrelated test data rather than the secret. |
| [screenshots/07a-automated-first-response.png](screenshots/07a-automated-first-response.png) | Initial automated attack produced an unrelated test case. |
| [screenshots/07-automated-attack-results.png](screenshots/07-automated-attack-results.png) | Two automated attacks; no exact secret leak in this run. |
| [screenshots/08-configuration-extraction-no-leak.png](screenshots/08-configuration-extraction-no-leak.png) | Three initial extraction strategies; no exact leaks in this run. |
| [screenshots/09-confirmed-secret-leak.png](screenshots/09-confirmed-secret-leak.png) | First automated exact disclosure; attack 3 revealed the fictional code. |
| [screenshots/09b-vulnerable-system-prompt-source.png](screenshots/09b-vulnerable-system-prompt-source.png) | Source screenshot showing the fictitious identifier embedded in system instructions. |
| [screenshots/12-allowed-vs-protected.png](screenshots/12-allowed-vs-protected.png) | Control experiment: model disclosed the fictional identifier when permitted (3/3), and withheld it when prohibited (0/3). |
| [screenshots/13a-identifier-disclosures-initial.png](screenshots/13a-identifier-disclosures-initial.png) | Identifier attack test found two exact disclosures among three approaches. |
| [screenshots/13-identifier-disclosure-evidence.png](screenshots/13-identifier-disclosure-evidence.png) | Full prompts, generated responses, and two confirmed exact disclosures. |
| [screenshots/14-defensive-test-results.png](screenshots/14-defensive-test-results.png) | Defensive test: same three adversarial prompts after removing the identifier from model context; 0/3 exact disclosures in this run. |

## Comparison highlights

- **Protected baseline (control):** 0/3 exact disclosures with the model instructed not to reveal a provided identifier.
- **Attacked vulnerable setup:** 2/3 different attack techniques disclosed that identifier once each.
- **Defensive setup:** 0/3 exact disclosures when the identifier was withheld from the model context.
- These are small independent test sets, not an estimated real-world breach probability. The defensive model still produced invented configuration details.

## Screenshots still needed

These appeared as pasted terminal output or were discussed, but **no matching screenshot image was uploaded in this chat**:

- `01-local-llm.png` — optional: Ollama launching `gemma3:1b` and answering a test prompt.
- `10-attack-repeatability.png` — five fresh sessions, **0/5** exact disclosures.
- `11-attack-strategy-comparison.png` — three strategies repeated three times, **0/9** exact disclosures.

Please capture the original terminal output when possible. If a rerun produces different results, record the new result honestly rather than labelling it as an earlier experiment. Avoid including real API keys, passwords, tokens, or personal information.

## Suggested GitHub README showcase

Use these images for a concise progression:

1. [Working chatbot](screenshots/02-python-chatbot.png)
2. [First baseline refusal](screenshots/04-baseline-refusal.png)
3. [Automated secret disclosure](screenshots/09-confirmed-secret-leak.png)
4. [Prompt and response evidence](screenshots/13-identifier-disclosure-evidence.png)
5. [Allowed versus protected controls](screenshots/12-allowed-vs-protected.png)
6. [Defensive design with zero disclosures in this run](screenshots/14-defensive-test-results.png)

For example, add the following to your repository's main `README.md`:

```markdown
### Red-team evidence
![RedLens AI identifier disclosure](screenshots/13-identifier-disclosure-evidence.png)

### Original vulnerable configuration
![Vulnerable system prompt](screenshots/09b-vulnerable-system-prompt-source.png)

### Controls and defensive comparison
![Allowed versus protected controls](screenshots/12-allowed-vs-protected.png)
![Defensive test results](screenshots/14-defensive-test-results.png)
```
