This animation is made on python using turtle graphic library.

Animation starts with a heart spin (credits to https://github.com/wgahnagl/valentine) and then makes a big red heart questioning "Will you be my valentine?" and a checkbox with two answers: "yes" or "no".

Click on "yes" starts an endless heart spam all around the screen. Unfortunate click on "no" writes "Error" on top of the heart. If they still refuse to be your valentine, second click on "no" changes text to "Please!". For the third time the heart turns black with text saying "It's a «no»", than the heart is breaking.

If you respect their refusal more than I did, you can change error() in str 93 to heSaidNo(). In this case you will need to comment or delite str 96 to str 112, and also a cycle if from def heSaidNo, which is str 118 to str 120. This way the heart will turn black right after first click on "no". 

If you are not ready to take a refusal at all, comment or delite everything from str 102 to str 150 and change "t.onscreenclick(undo, btn=1, add=None)" to  "t.onscreenclick(yesOrYes, btn=1, add=None)" in str 100.

I really hope that this program will make them say "yes" or at least smile.

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=FF69B4F7&random=false&width=435&lines=Have+fun+%3C3)


