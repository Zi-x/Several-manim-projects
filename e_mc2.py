from manimlib.imports import *
import math
class title(Scene):
    def construct(self):


        #Make quto
        self.wait(0.1)
        quto  = Text("Everything should be made as simple as possible",font="Segoe Print")
        quto2 = Text("but not simpler",font="Segoe Print")
        quto.set_stroke(width=0.42);quto2.set_stroke(width=0.42)
        quto2.scale(0.45)
        quto.scale(0.45)
        emc   = TexMobject("E=mc^2")
        emc.scale(2.85)
        emc.shift(UP*1.01)
        quto.next_to(quto,DOWN*2.62)
        quto2.next_to(quto,DOWN)
        name = Text("A.Einstein",font="Segoe Print")
        name.set_stroke(width=0.4)
        name.scale(0.4)
        name.shift(DOWN*3.6+RIGHT*5.9)
        
        self.play(FadeInFrom(emc,UP))
        self.wait(1.1)
        self.play(Write(quto),run_time=4.1)
        self.play(Write(quto2),run_time=2)
        self.play(Write(name),run_time=1.6)
        self.wait(3)

class pre(Scene):
    def construct(self):
        #object
        line1=Line(np.array([-1.6,0.9,0]),np.array([1.6,0.9,0]))
        line2=Line(np.array([-1.6,-0.9,0]),np.array([1.6,-0.9,0]))
        cirpoint=Dot(color=YELLOW)
        cirpoint.scale(0.83)
        cirpoint.flip()
        Gc=VGroup(cirpoint,line1,line2)
        colorswhite = color_gradient([BLACK,WHITE],10)
        colorsyellow = color_gradient(["#6C6C00",YELLOW],10)
        arrow1 = Arrow(np.array([-0.5,0,0]),np.array([0.3,0,0]),buff=0.17)
        text_v = TexMobject("v")
        text_v.scale(0.8)
        text_v.next_to(arrow1,RIGHT*0.5)
        arrow1g=VGroup(arrow1,text_v)

        #animation0
        Gccopy = Gc.copy()
        self.play(ShowCreation(Gccopy[1:]))
        self.play(ShowCreation(Gccopy[0]),run_time=1.2)
        self.wait(2)
        cirpointcopy = Gccopy[0].copy()
        cirpointcopy.next_to(Gccopy[2],UP*0.046)
        self.play(FadeOut(Gccopy[0]))
        self.wait(0.2)
        self.play(FadeIn(cirpointcopy))
        self.wait(0.5)
        for i in range(5):
            self.play(cirpointcopy.shift,UP*8*0.2062,rate_func=there_and_back,run_time=1.1)
        #self.play(cirpointcopy.shift,UP*7*0.2062,run_time=0.65)
        self.play(FadeOut(Gccopy[1:],run_time=0.85),FadeOutAndShift(cirpointcopy,UP*5*0.206,run_time=0.6))
        self.wait(1)
        #position
        Gc.shift(UP*2.2+LEFT*3.7)
        cirpoint.next_to(line2,UP*0.046)
        arrow1g.shift(LEFT*4.7+UP*0.85)


        for i in range(8):
            if(i<7):
                cirpoint.set_color(colorsyellow[i+2])
                Gc[1:3].set_color(colorswhite[i+2])
            else:
                cirpoint.set_color(colorsyellow[9])
                Gc[1:3].set_color(colorswhite[9])
            if(i<1):
                self.play(ApplyMethod(Gc[1:3].shift,0).copy(),
                ApplyMethod(cirpoint.shift,0).copy())
                self.play(ShowCreation(arrow1g[0]),Write(arrow1g[1]))
            
            self.play(ApplyMethod(Gc[1:3].shift,RIGHT*0.9,rate_func=linear).copy(),
            ApplyMethod(cirpoint.shift,UP*0.2055+RIGHT*0.9,rate_func=linear).copy(),run_time=0.9)
            Gc[1:3].shift(RIGHT*0.9)
            cirpoint.shift(UP*0.2055+RIGHT*0.9)
        #animation2
        xuxain0=DashedLine(np.array([0,0.85,0]),np.array([0,-0.9,0]))
        xuxain0.shift(UP*2.2+RIGHT*3.5)
        text01 = TexMobject("ct","vt","ct'")
        text01[2].next_to(xuxain0,RIGHT);text01[2].shift(UP*0.1)
        text01[1].shift(UP*0.95)
        text01[0].shift(UP*2.66+RIGHT*0.1)
        text01[0].rotate(PI/(9.6))

        text02 = TexMobject("(vt)^2","+","(ct')^2","=","(ct)^2",color=RED)
        text02[3].set_color(WHITE)
        text02.shift(LEFT*1.35+DOWN*0.35)

        text03 = TexMobject("(ct')^2","=","(ct)^2","-","(vt)^2",color=RED)
        text03[1].set_color(WHITE)
        text03.next_to(text02[3],DOWN*2.9,submobject_to_align=text03[1])

        text04 = TexMobject("t\\ ","=","\\frac{t'}{\\sqrt{1-\\frac{v^2}{c^2}}}",color=RED)
        text04[1].set_color(WHITE)
        text04[0].scale(1.15)
        text04.next_to(text03[1],DOWN*3.1,submobject_to_align=text04[1])

        text05a  = TextMobject("洛伦兹因子")
        text05a.scale(1.15)
        text05b  = TexMobject("\gamma","=","\\frac{1}{\\sqrt{1-\\frac{v^2}{c^2}}}")
        text05b.scale(0.95)
        text05b.next_to(text05a,DOWN*0.7,aligned_edge=ORIGIN)
        text05   = VGroup(text05a,text05b)
        text05.bg=BackgroundRectangle(text05,fill_color=PINK,fill_opacity=0.7,buff=0.05)
        text05group   = VGroup(text05.bg,text05)
        text05group.scale(0.65)
        text05group.shift(LEFT*5+DOWN*1.36)

        self.play(Write(xuxain0))
        self.wait(2)
        self.play(Write(text01[1]))
        self.wait(1)
        self.play(Write(text01[0]))
        self.wait(1)
        self.play(Write(text01[2]))
        self.wait(2)
        self.play(Write(text02))
        self.wait(1)
        self.play(Write(text03))
        self.wait(1)
        self.play(Write(text04[0]));self.play(Write(text04[1:]),run_time=3)
        self.wait(1)
        self.play(Write(text05group),run_time=2.2)
        self.wait(5)



class mid(Scene):
    def construct(self):
        formula01 = TexMobject("E_{k}","=","\\int_{0}^{x}Fdx")
        formula01.scale(0.55)
        formula01.shift(UP*3.28+LEFT*5.7)

        tip01     = TexMobject("\\because","Ft=mv",color=RED)
        tip01.scale(0.5)
        tip01.next_to(formula01,DOWN)
        
        formula02 = TexMobject("=","\\int_{0}^{x}\\frac{d}{dt}(mv)d(vt)",
                    "=","\\int_{0}^{t}\\frac{d}{dt}(mv)vdt","=",
                    "\\int_{0}^{mv}\\frac{dt}{dt}vd(mv)")
        formula02.scale(0.55)
        formula02.next_to(formula01[1],DOWN*5.2,submobject_to_align=formula02[0])
        

        tip02     = TexMobject("\\because","P=mv=\\frac{m_{0}\Delta{x}}{\Delta{t_{0}}}","=",
                                "\\frac{m_{0}\Delta{x}}{\Delta{t}}",
                                "\\times\\frac{\Delta{t}}{\Delta{t_{0}}}",color=RED)  
        tip02.scale(0.45)
        tip02.next_to(tip01[0],DOWN*6,submobject_to_align=tip02[0])

        tip03     = TexMobject("=","\\frac{m_{0}\Delta{x}}{\Delta{t}}",
                                "\\times\\frac{1}{\\sqrt{1-\\frac{v^2}{c^2}}}",color=RED)
        tip03.scale(0.45)                        
        tip03.next_to(tip02[2],DOWN*3,submobject_to_align=tip03[0])

        tip04     = TexMobject("=","\\frac{m_{0}}{\\sqrt{1-\\frac{v^2}{c^2}}}",
                                "\\times\\frac{\Delta{x}}{\Delta{t}}",color=RED)
        tip04[2].next_to(tip04[1],RIGHT)
        tip04[2].shift(UP*0.02)
        tip04.scale(0.45)                        
        tip04.next_to(tip03[0],DOWN*3,submobject_to_align=tip04[0])    

        tip05     = TexMobject("=","\\frac{m_{0}}{\\sqrt{1-\\frac{v^2}{c^2}}}",
                                "\\times{v}",color=RED)
        tip05[2].next_to(tip05[1],RIGHT)
        tip05[2].shift(UP*0.02)
        tip05.scale(0.45)                        
        tip05.next_to(tip04[0],DOWN*3,submobject_to_align=tip05[0])

        #tip06     = TexMobject("=","\\frac{m_{0}}{\\sqrt{1-\\frac{v^2}{c^2}}}\\times{v}")
        #tip06.scale(0.45)                        
        #tip06.next_to(tip05[0],DOWN*2.3,submobject_to_align=tip06[0])
        tip06     = TexMobject("\\Rightarrow","m","=",
                                "\\frac{m_{0}}{\\sqrt{1-\\frac{v^2}{c^2}}}",color=YELLOW)
        tip06.scale(0.525) 
        tip06.next_to(tip05[0],DOWN*3.6,submobject_to_align=tip06[2])

        formula03 = TexMobject("=",
                                "\\int_{0}^{v}vd(\\frac{m_{0}v}{\\sqrt{1-\\frac{v^2}{c^2}}})")
        formula03.scale(0.55)
        formula03.next_to(formula02[4],DOWN*3.7,submobject_to_align=formula03[0])

        formula04 = TexMobject("=",
                                "\\begin{bmatrix}\\frac{m_{0}v^2}{\sqrt{1-\\frac{v^2}{c^2}}}\\end{bmatrix}_{0}^{v}",
                                "-","\\int_{0}^{v}\\frac{m_{0}v}{\\sqrt{1-\\frac{v^2}{c^2}}}dv")
        formula04[1].scale(1.1)
        formula04.scale(0.55)
        formula04.next_to(formula03[0],DOWN*4.1,submobject_to_align=formula04[0])

        formula05 = TexMobject("=",
                                "\\frac{m_{0}v^2}{\\sqrt{1-\\frac{v^2}{c^2}}}","-",
                                "\\begin{bmatrix}-m_{0}c^2\\sqrt{1-\\frac{v^2}{c^2}}\,\\end{bmatrix}_{0}^{v}")
        formula05.scale(0.55)
        formula05.next_to(formula04[0],DOWN*3.8,submobject_to_align=formula05[0])

        formula06 = TexMobject("=",
                               "\\frac{m_{0}c^2}{\\sqrt{1-\\frac{v^2}{c^2}}}","-",
                                "m_{0}c^2")
        formula06.scale(0.55)
        formula06.next_to(formula05[0],DOWN*3.9,submobject_to_align=formula06[0])

        formula07 = TexMobject("=","mc^2","-","m_{0}c^2")
        formula07.scale(0.55)
        formula07.next_to(formula06[0],DOWN*3.75,submobject_to_align=formula07[0])
        ###sum
        formula08 = TexMobject("E_{k}","=","mc^2-m_{0}c^2",color="#FF69B4")
        formula08.scale(0.75)
        #formula08[1].set_color(WHITE)
        formula08.shift(UP*3.05+RIGHT*4.8)

        formula08a = TexMobject("E_{k}","=","E\,-\,E_{0}",color="#FF69B4")
        #formula08a[1].set_color(WHITE)
        formula08a.scale(0.75)
        formula08a.next_to(formula08[1],DOWN*2,submobject_to_align=formula08a[1])

        formula09 = TexMobject("E\\,\\,","=","mc^2",color="#FF69B4")
        formula09[0].shift(LEFT*0.041)
        #formula09[1].set_color(WHITE)
        formula09.scale(0.75)
        formula09.next_to(formula08a[1],DOWN*2,submobject_to_align=formula09[1])

        formula10 = TexMobject("E_{0}","=","m_{0}c^2",color="#FF69B4")
        formula10[0].shift(LEFT*0.018)
        #formula10[1].set_color(WHITE)
        formula10.scale(0.75)
        formula10.next_to(formula09[1],DOWN*2,submobject_to_align=formula10[1])
        formu8a910s = VGroup(formula08,formula08a,formula09,formula10)
        formu8a910s.bg=SurroundingRectangle(formu8a910s,color=WHITE,buff=0.2)
        formu8a910s.bg.set_stroke(width=2.1)
        
        #animation3
        self.play(Write(formula01))
        self.wait(1)
        self.play(Write(tip01))
        self.wait(1)
        self.play(Write(formula02),run_time=6.2)
        self.wait(3.6)
        self.play(Write(tip02),run_time=3.5)
        self.wait(2)
        self.play(Write(tip03))
        self.wait(1.5)
        self.play(Write(tip04))
        self.wait(1.5)
        self.play(Write(tip05))
        self.wait(1.5)
        self.play(Write(tip06))
        self.wait(2)
        self.play(Write(formula03),run_time=2.2)
        self.wait(2)
        self.play(Write(formula04),run_time=4.5)
        self.wait(2)
        self.play(Write(formula05),run_time=3)
        self.wait(2)
        self.play(Write(formula06),run_time=2.5)
        self.wait(1.5)
        self.play(Write(formula07))
        self.wait(3)
        self.play(Write(formula08),run_time=2.2)
        self.wait(1.5)
        self.play(Write(formula08a),run_time=2.2)
        self.wait(1.5)
        self.play(Write(formula09),run_time=2.2)
        self.wait(1.5)
        self.play(Write(formula10),run_time=2.2)
        self.wait(1)
        self.play(ShowCreation(formu8a910s.bg),run_time=1.8)
        self.wait(1)

        #Making object heart
        circle01=Circle(fill_color="#FF2093",color="#FF2093",fill_opacity=0.5)
        circle02=Circle(fill_color="#FF2093",color="#FF2093",fill_opacity=0.5)
        square01=Square(fill_color="#FF2093",color="#FF2093",fill_opacity=0.5)
        love=VGroup(circle01,circle02,square01)
        
        #position
        circle01.shift((UP+LEFT)*np.sqrt(2)/2)
        circle02.shift((UP+RIGHT)*np.sqrt(2)/2)
        square01.rotate(np.pi/4)
        #Showing object
        love.scale(0.72)
        love.shift(RIGHT*4.7+DOWN*2.5)
        self.play(ShowCreation(circle01),ShowCreation(circle02),ShowCreation(square01),run_time=1.2)
        self.wait(1)
        self.play(ApplyMethod(love.set_opacity,1))
        self.wait(3)

        


