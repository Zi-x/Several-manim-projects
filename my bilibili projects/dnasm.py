from manimlib.imports import *
import math
import random
class nda1(Scene):
    def construct(self):
        random.seed(44)
        line1s = VGroup()
        for i in range(11):
            linee = Line(start=[-6+1.2*i,2.5,0],end=[-6+1.2*i,2.5+0.05*random.uniform(10,24),0])
            linee.set_stroke(width=3.3)
            linee.set_color(YELLOW)
            line1s.add(linee)
        line2s = VGroup()
        for i in range(11):
            linee = Line(start=[-6+1.2*i,0.7,0],end=[-6+1.2*i,0.7+0.05*random.uniform(10,26),0])
            linee.set_stroke(width=3.3)
            linee.set_color(YELLOW)
            line2s.add(linee)
        line3s = VGroup()   
        for i in range(11):
            linee = Line(start=[-6+1.2*i,-1.3,0],end=[-6+1.2*i,-1.3+0.05*random.uniform(9,27),0])
            linee.set_stroke(width=3.3)
            linee.set_color(YELLOW)
            line3s.add(linee)
        line4s = VGroup()   
        for i in range(11):
            linee = Line(start=[-6+1.2*i,-3.0,0],end=[-6+1.2*i,-3.0+0.05*random.uniform(11,22),0])
            linee.set_stroke(width=3.3)
            linee.set_color(YELLOW)
            line4s.add(linee)
        for i in range(11):
            self.play(ShowCreation(line1s[i]),ShowCreation(line2s[i]),ShowCreation(line3s[10-i]),ShowCreation(line4s[10-i]),run_time=0.56)
        self.wait(3)
        line1_4s = VGroup(line1s,line2s,line3s,line4s)
        line_18ups = VGroup()
        line_18downs = VGroup()
        for i in range(4):
            for j in range(11):
                if(line1_4s[i][j].get_length()>18*0.05):
                    line_18ups.add(line1_4s[i][j])
                else:
                    line_18downs.add(line1_4s[i][j])
        #number18up = len(line_18ups)-1
        self.play(ApplyMethod(line_18ups.set_color,GRAY),run_time=1.2)
        self.wait(1)
        self.play(FadeOut(line_18ups))
        self.wait(4)
        self.play(FadeOut(line_18downs))

        
        l2ine1s = VGroup()
        for i in range(11):
            l2inee = Line(start=[-6+1.2*i,2.5,0],end=[-6+1.2*i,2.5+0.05*random.uniform(5,18),0])
            l2inee.set_stroke(width=3.3)
            l2inee.set_color(YELLOW)
            l2ine1s.add(l2inee)
        l2ine2s = VGroup()
        for i in range(11):
            l2inee = Line(start=[-6+1.2*i,0.7,0],end=[-6+1.2*i,0.7+0.05*random.uniform(5,18),0])
            l2inee.set_stroke(width=3.3)
            l2inee.set_color(YELLOW)
            l2ine2s.add(l2inee)
        l2ine3s = VGroup()   
        for i in range(11):
            l2inee = Line(start=[-6+1.2*i,-1.3,0],end=[-6+1.2*i,-1.3+0.05*random.uniform(4,17),0])
            l2inee.set_stroke(width=3.3)
            l2inee.set_color(YELLOW)
            l2ine3s.add(l2inee)
        l2ine4s = VGroup()   
        for i in range(11):
            l2inee = Line(start=[-6+1.2*i,-3.0,0],end=[-6+1.2*i,-3.0+0.05*random.uniform(5,17),0])
            l2inee.set_stroke(width=3.3)
            l2inee.set_color(YELLOW)
            l2ine4s.add(l2inee)
        l2ine1_4s = VGroup(l2ine1s,l2ine2s,l2ine3s,l2ine4s)
        self.play(FadeIn(l2ine1_4s))
        self.wait()
        line_12ups = VGroup()
        line_12downs = VGroup()
        for i in range(4):
            for j in range(11):
                if(l2ine1_4s[i][j].get_length()>12*0.05):
                    line_12ups.add(l2ine1_4s[i][j])
                else:
                    line_12downs.add(l2ine1_4s[i][j])
        #number18up = len(line_18ups)-1
        self.play(ApplyMethod(line_12ups.set_color,GRAY),run_time=1.2)
        self.wait(1)
        self.play(FadeOut(line_12ups))
        self.wait(3)
        self.play(FadeOut(line_12downs))
        
        l3ine1s = VGroup()
        for i in range(11):
            l3inee = Line(start=[-6+1.2*i,2.5,0],end=[-6+1.2*i,2.5+0.05*random.uniform(3,12),0])
            l3inee.set_stroke(width=3.3)
            l3inee.set_color(YELLOW)
            l3ine1s.add(l3inee)
        l3ine2s = VGroup()
        for i in range(11):
            l3inee = Line(start=[-6+1.2*i,0.7,0],end=[-6+1.2*i,0.7+0.05*random.uniform(4,11),0])
            l3inee.set_stroke(width=3.3)
            l3inee.set_color(YELLOW)
            l3ine2s.add(l3inee)
        l3ine3s = VGroup()   
        for i in range(11):
            l3inee = Line(start=[-6+1.2*i,-1.3,0],end=[-6+1.2*i,-1.3+0.05*random.uniform(3,12),0])
            l3inee.set_stroke(width=3.3)
            l3inee.set_color(YELLOW)
            l3ine3s.add(l3inee)
        l3ine4s = VGroup()   
        for i in range(11):
            l3inee = Line(start=[-6+1.2*i,-3.0,0],end=[-6+1.2*i,-3.0+0.05*random.uniform(4,13),0])
            l3inee.set_stroke(width=3.3)
            l3inee.set_color(YELLOW)
            l3ine4s.add(l3inee)
        l3ine1_4s = VGroup(l3ine1s,l3ine2s,l3ine3s,l3ine4s)
        self.play(FadeIn(l3ine1_4s))
        
        self.wait(5)


                

        
                
