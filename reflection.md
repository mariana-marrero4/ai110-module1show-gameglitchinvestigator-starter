# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  At first look it was normal, even though the developer debug info section caught me off gaurd because it was open to the player to see. Other than that I noticed that when you press enter for what I suppose is submiting your answer it doesn't and the hints are broken. I also tried to generate a new game  but it did not work so I had to refresh the page every time I won and the range of difficulty is also broken. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  -- The hints are backwards
  -- Accepts negative numbers
  -- The difficulty attemps available is wrong, having easy being more difficult than normal, meaning less attemps available
  -- Ranges of difficulty might be inverted with normal havng a bigger range than hard

  Other bugs found after asking AI about code:
  -- The message "Guess a number between 1 and 100" always stays the same even after chaging the difficulty mode
  -- New game does not respect the difficulty so the secret number is always chosen between 1-100


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used a mix of the Copilot Chat in VS Code and Claude on my web browser. I mostly worked with the Copilot Chat to help with bug fixes and the refactoring. On the other hand, I used Claude fro any problem I faced with running the program and installing dependencies. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).  #TODO-finish answering

A correct AI suggestion would be when I asked it to help with refactoring and update the inputs. It changed thing correctly and I double checked for any mistakes or redundant information. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


A misleading AI suggestion was when I asked to create the test to verify if the hints were working right it created another file and a new test that were redundant. I verified the result by double checking the code and asking the AI if the new test was necesary along with the new file. After the AI deemed it unnecesary it deleted them.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
