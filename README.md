This animation is made on python using turtle graphic library. To run it you will need to install python from https://www.python.org/downloads/.

Animation starts with a heart spin (shout out to https://github.com/wgahnagl/valentine) and then makes a big red heart with the question "Will you be my valentine?" and a checkbox with two answers: "yes" or "no".

If they click into "yes" box, it starts an endless heart spam all around the screen. If they, unfortunately, click into "no" box, it writes "Error" on top of the heart. If they make the same mistake again, the text changes to "Please!". And for the third time the heart turns black with text saying "It's a «no»", and than the heart is breaking.

If you respect their refusal more than I did, you can change error() in str 93 to heSaidNo(). In this case you will need to comment or delite str 96 to str 112, and also a cycle if from def heSaidNo, which is str 118 to str 120. This way the heart will turn black  

If you are not ready to take a refusal at all, comment or delite everything from str 102 to str 150 and change "t.onscreenclick(undo, btn=1, add=None)" to  "t.onscreenclick(yesOrYes, btn=1, add=None)" in str 100.

I really hope that this program will make them say "yes" or at least smile.

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=FF69B4F7&random=false&width=435&lines=Have+fun+%3C3)


