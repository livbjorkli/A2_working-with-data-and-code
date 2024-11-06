#size of the canvas
size(800, 500);

#resize tree to middle
translate(width/2 - 100, height/2 - 100)

#paint background white
background (255, 255, 255)

#text in background (sky)
#Black text color
fill(0) 
#size of font
textSize (20)
text("6", 100, -60)

#ground
stroke (0)
strokeWeight (1)
line (-400, 270, 600, 270)

#left tree
#draw the stem of the tree
fill (255, 255, 255)
rect (50, 190, 100, 250)

#putting in text (colour and font size)
#black text colour 
fill(0)
#text size
textSize (20)

#Number 3 for the stem of the tree 
text ("3", 100, 305)


#tree triangles 
# bottom triangle tree
fill (255, 255, 255)
triangle (0, 190, 200, 190, 100, 80)

#Number 4 for the bottom tree
fill (0)
text ("4", 100, 180)

# middle triangle tree
fill (255, 255, 255)
triangle (10, 130, 190, 130, 100, 30)

#Number 4 for the middle tree
fill (0)
text ("4", 100, 100)

#top triangle tree
fill (255, 255, 255)
triangle (20, 80, 180, 80, 100, 0)

#Number 4 for the top tree
fill (0)
text ("4", 100, 50)

#putting in text (colour and font size)
#black text colour 
fill(0)
#text size
textSize (20)

#Number 2 for the ground 
text ("2", 300, 300)
text ("2", -100, 300)

#butterfly 
fill (255, 255, 255)
stroke (0)
strokeWeight (1)

#rotate butterfly - https://processing.org/reference/rotate_.html
rotate (PI/3.10)

#left wing of butterfly
ellipse (30, 100, 30, 50)
#antenna on left butterfly 
#left
stroke (0)
strokeWeight (1)
line (45, 90, 35, 70)
#right
line (45, 90, 55, 70)
#right wing of butterfly 
ellipse (60, 100, 30, 50)


#body of butterfly 
stroke (0)
strokeWeight (1)
line (45, 90, 45, 110)

#butterfly on the right 
#left wing
fill (255)
stroke (0)
strokeWeight (1)
ellipse (30, 0, 30, 40)
#right wing
ellipse (60, 0, 30, 40)
#antenna on right butterfly 
#left
stroke (0)
strokeWeight (1)
#left
line (45, -10, 40, -30)
#right
line (45, -10, 50, -30)

#body of butterfly on the right
stroke (0) 
strokeWeight (1)
line (45, -15, 45, 15)

#putting in text (colour and font size)
#black text colour 
fill(0)
#text size
textSize (20)

#Number "1" in the left wing of the right butterfly 
text ("1", 24, 8)

#Number "1" in the right wing of the right butterfly 
text ("1", 55, 8)

#Number "1" in the left wing of the left butterfly 
text ("1", 24, 108)

#Number "1" in the right wing of the right butterfly 
text ("1", 55, 108)


#Adding the shape of an eclipse to be a sun in the left corner
fill (255)
stroke (0)
ellipse (-160, 125, 130, 130)

#rotate number 5 - https://processing.org/reference/rotate_.html
rotate (PI/0.6)

#add text "5" in sun
fill(0)
textSize (17)
text ("5", -195, -75)

#adding text in top right for key colours 
#Black text color
fill(0) 
#size of font
textSize (20)

#keys of colours
text("1 = yellow", 380, -110)
text ("2 = light green", 380, -90)
text ("3 = brown", 380, -70)
text ("4 = dark green", 380, -50)
text ("5 = orange", 380, -30)
text ("6 = light blue", 380, -10)
