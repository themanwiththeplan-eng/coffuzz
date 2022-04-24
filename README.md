# Cofuzz 

This is a lightweight utility that will allow you to quickly fuzz any url that's given using two positional arguments.

---

## Use Case

Currently it is set up so that after calling the script using python3 you are able to supply and arg[1] (URL) and arg[2] (Filepath). Similar to other fuzzers it will take the filepath
and iterate through that list. arg[1] should be formatted as a url i.e, http://something.com. 

---

## Future Functionality

In the future I plan on making this utility similar to cURL in the way that you are able to specify what kind of request you would like to make. This way you're able to
fuzz and automate the process of inline SQLi, XSS, and other things that require you to execute arbitrary "code." With that being said currently this is very barebones
and will work in the case of injection on a GET parameter. 

---

## Why I Made It

I made this simply because, number one I wanted to have something the community could use easily and hopefully contribute to as this is public and anybody can make changes
to it, but also because the other security tools that people use for fuzzing seem to have a lot of functionality while also at the same time adding more complexity.

---

## How To Use

You can make a bash alias in your .bashrc for this by calling <alias> = "python3 <filepath>."

Ensure that you source it by using source ~/.bashrc.

This will simply allow you to use it globally in any filepath that you'd like and from there you're ready just use arg[1] as a URL and arg[2] as a filepath.
