# Python Hailstone Problem:

This is a working Python program that shows the Hailstone Problem in action and details what its doing to bring you to the final solution, which is as far as we can tell, always 1.

------

## What is the Hailstone Problem?

The Hailstone Problem (also known as the Collatz Conjecture as well as many other names) is an infamous problem that says if you pick any positive integer and feed that into a statement which divides the number by two if its even and multiply it by three and one if its odd, then feed the output of that statement back into the statement continuously, you will possibly, eventually reach the lowest number that may be given from that statement which is one. So far there isn't a solution to the problem and every positive integer we have tried will result in one. If you manage to get any other number than one, congratulations! You have either found a solution to the problem or a bug in my code (probably the latter). If you wish to learn more watch [this video](https://youtu.be/094y1Z2wpJg) by [Veritasium.](https://www.youtube.com/channel/UCHnyfMqiRRG1u-2MsSQLbXA)

------

## The Hailstone Problem in Pseudocode:

```pseudocode
Number ← USERINPUT 
While Number != 1
	if Number % 2
		Number = Number / 2
	else
		Number = 3 * Number + 1
EndWhile
```
------
## Features:

- Choice of using a random number by just not entering a number.
- Optionally saving output to a text file.
- Horribly written code that doesn't contain a single comment.
- That is all.

------
## Python Version?

I don't know how interoperable Python versions are but I created and tested it in Python 3.8.3. If anyone would like to inform me on how interoperable Python programs are go ahead.

------

## License:

This program is published under the MIT License and it can be found under [LICENSE](LICENSE) in the root directory of this repository.