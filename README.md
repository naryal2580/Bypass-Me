# Bypass Me

This is a simple CTF challenge to byapass path traversal. Flag is just there as a placeholder and, to provide a dopamine kick to the person who bypassed it. Payload is what you're supposed to submit.

If you can bypass it, do raise an Issue.

And, if you have a better fix. Send a PR :)

**RED vs BLUE**

Solve it, and get listed below.

##### RED
 - @C15C01337 (PAYLOAD: `/?filename=../flag/flag.txt`) **PATCHED**
 - @guragainroshan0 (PAYLOAD: `/?filename=./....//flag/flag.txt`)

##### BLUE
 - @naryal2580 (Monkey patch: `filepath = f'./root/{filename}'.replace('../', '').replace('..\\', '').rstrip('/').rstrip('\\')`) **GOT BYPASSED**
