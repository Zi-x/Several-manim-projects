from manimlib.imports import *
import math
class cuopaifirst(Scene):
    def construct(self):
        ne = TexMobject("\\frac{n!}{e}")
        ne.scale(2.25)
        textitle= TextMobject("错排问题")
        textitle.scale(2)
        textitle.shift(UP*1.5)
        ne.shift(DOWN*0.6)
        self.play(Write(textitle))
        self.wait()
        self.play(Write(ne))
        self.wait(2)

class cuopai(Scene):
    def construct(self):
        
        colorgroup = [PINK,GREEN,"#9400D3",YELLOW,BLUE,ORANGE,WHITE]
        #making object--正方形
        squgroup   = VGroup()
        for i in range(7):
            squ_i = Square(side_length=1.15)
            squ_i.shift(RIGHT*1.6*(i-3))
            squ_i.set_color(colorgroup[i])
            squgroup.add(squ_i)
        squgroup[0:2].shift(LEFT*0.8)
        squgroup[5:7].shift(RIGHT*0.8)
        textdots = TexMobject("\\dots","\\dots")
        textdots[0].next_to(squgroup[1],RIGHT*1.5)
        textdots[1].next_to(squgroup[4],RIGHT*1.5)

        firstgroup=VGroup(squgroup,textdots)
        firstgroup.to_edge(UP);firstgroup.shift(UP*0.2)

        #making object--圆,number
        textnumber  = TexMobject("1","2","k-1","k","k+1","n-1","n")
        textnumber.scale(0.56)
        cirgroup    = VGroup()
        numbergroup = VGroup()
        for i in range(7):
            cir_i = Circle(radius=squ_i.get_width()/2.2,color=colorgroup[i],
            fill_color=colorgroup[i],fill_opacity=1)
            cir_i.shift(RIGHT*1.6*(i-3))
            textnumber[i].next_to(cir_i,DOWN*0.65)  
            numbergroup.add(textnumber[i])
            cirgroup.add(cir_i)
        cirgroup[0:2].shift(LEFT*0.8);numbergroup[0:2].shift(LEFT*0.8)
        cirgroup[5:7].shift(RIGHT*0.8);numbergroup[5:7].shift(RIGHT*0.8)
        textdots2 = TexMobject("\\dots","\\dots")
        textdots2[0].next_to(cirgroup[1],RIGHT*1.5)
        textdots2[1].next_to(cirgroup[4],RIGHT*1.5)
        cirgroup.shift(UP*0.3);textdots2.shift(UP*0.3);numbergroup.shift(UP*0.3);numbergroup[6].shift(DOWN*0.041)        
        #animation0
        self.play(FadeIn(squgroup[0]),run_time=0.76)
        self.play(FadeIn(squgroup[1]),run_time=0.76)
        self.play(ShowCreation(textdots[0]),run_time=0.76)
        for i in range(3):
            self.play(FadeIn(squgroup[2+i]),run_time=0.76)
        self.play(ShowCreation(textdots[1]),run_time=0.76)
        self.play(FadeIn(squgroup[5]),run_time=0.76)
        self.play(FadeIn(squgroup[6]),run_time=0.76)
        
        self.wait(0.5)
        self.play(FadeIn(cirgroup[0]),run_time=0.76)
        self.play(FadeIn(cirgroup[1]),run_time=0.76)
        self.play(ShowCreation(textdots2[0]),run_time=0.76)
        for i in range(3):
            self.play(FadeIn(cirgroup[2+i]),run_time=0.76)
        self.play(ShowCreation(textdots2[1]),run_time=0.76)
        self.play(FadeIn(cirgroup[5]),run_time=0.76)
        self.play(FadeIn(cirgroup[6]),run_time=0.76)
        self.wait(0.5)

        for i in range(7):
            self.play(Write(numbergroup[i]),run_time=0.75)
        self.wait()

        #xuxian0
        xuxian0 = DashedLine(cirgroup[0].get_edge_center(UP),squgroup[0].get_edge_center(DOWN))
        xuxiangroup   = VGroup()
        for i in range(7):
            if(i<6):
                xuxian_i = DashedLine(cirgroup[0+i].get_edge_center(UP),
                squgroup[1+i].get_edge_center(DOWN))
            if(i>=6):
                xuxian_i = DashedLine(cirgroup[6].get_edge_center(UP),
                squgroup[0].get_edge_center(DOWN))
            xuxiangroup.add(xuxian_i)
        #animation1
        self.wait(0.5)
        cross = TexMobject("\\times",color="#FF0000")
        cross.flip()
        cross.scale(2)
        cross.move_to(xuxian0)
        self.play(ShowCreation(xuxian0))
        self.wait(1)
        self.play(ShowCreation(cross))
        self.wait(1)
        self.play(FadeOut(cross),FadeOut(xuxian0))
        self.wait(1)
        for i in range(6):
            self.play(ShowCreation(xuxiangroup[i]),run_time=0.72)
        self.play(ShowCreation(xuxiangroup[6]),run_time=1)
        self.wait(3)
        self.play(FadeOut(xuxiangroup))

        texttuidao = TextMobject("现在我们设n个球n个盒子时方案数为$D_{n}$",
                                "对方案数$D_{n}$做分类讨论：\\\\","$\\bullet\\ $n号球放进1号盒子",
                                "$\\bullet\\ \\dots$","$\\bullet\\ $n号球放进k号盒子",
                                "$\\bullet\\ \\dots$\\\\","$\\bullet\\ $n号球放进n-1号盒子")
        texttuidao[0].scale(0.52);texttuidao[1:].scale(0.51)
        
        texttuidao[0].shift(LEFT+DOWN*1.65)
        texttuidao[1].next_to(texttuidao[0],DOWN*0.8,aligned_edge=LEFT)
        texttuidao[2].next_to(texttuidao[1],RIGHT)
        texttuidao[3].next_to(texttuidao[2],DOWN,aligned_edge=LEFT)
        texttuidao[4].next_to(texttuidao[3],DOWN,aligned_edge=LEFT)
        texttuidao[5].next_to(texttuidao[4],DOWN,aligned_edge=LEFT)
        texttuidao[6].next_to(texttuidao[5],DOWN,aligned_edge=LEFT)

        texttuidao2= TextMobject("$\\bullet\\ $对k号球\\\\","$\\circ\\ $k号球放进了n号箱子",
                                    "$\\circ\\ $k号球没有放进了n号箱子")
        texttuidao2.scale(0.46)
        texttuidao2[0].move_to(texttuidao[3])
        texttuidao2[0].shift(RIGHT*3.75+UP*0.02)
        texttuidao2[1].next_to(texttuidao2[0],DOWN,aligned_edge=LEFT)
        texttuidao2[1].shift(RIGHT*0.15)
        texttuidao2[2].next_to(texttuidao2[1],DOWN,aligned_edge=LEFT)

        textn_2 = TextMobject("$\\rightarrow(D_{n-2}$种方案)")
        textn_2.scale(0.45);textn_2.next_to(texttuidao2[1],RIGHT*0.5)
        textn_1 = TextMobject("$\\rightarrow(D_{n-1}$种方案)")
        textn_1.scale(0.45);textn_1.next_to(texttuidao2[2],RIGHT*0.5)


        self.play(Write(texttuidao[0]))
        self.wait(1.5)
        self.play(Write(texttuidao[1]))
        self.wait(1)
        for i in range(5):
            self.play(Write(texttuidao[i+2]))
            self.wait(0.2)
        self.wait(1)
        brace01 = Brace(texttuidao2,LEFT)
        brace01.scale(0.95)
        self.play(ShowCreation(brace01))
        self.play(ApplyMethod(cirgroup[6].move_to,squgroup[3]),run_time=1.5)
        self.wait(1)
        self.play(Write(texttuidao2[0]))
        self.wait(1)
        self.play(Write(texttuidao2[1]))
        self.wait(1)
        cirposition = cirgroup[3].get_center()
        self.play(ApplyMethod(cirgroup[3].move_to,squgroup[6]),run_time=1.5)
        self.wait(1)
        self.play(Write(textn_2))
        self.wait(1.5)
        self.play(Write(texttuidao2[2]))
        self.wait(1)
        self.play(ApplyMethod(cirgroup[3].move_to,cirposition),run_time=1.5)
        self.wait(1)
        self.play(Write(textn_1))
        self.wait(2.3)

        textntran = TextMobject("$D_{n-2}+D_{n-1}$种方案")
        textntran.scale(0.55)
        textntran.move_to(texttuidao2[1])
        texttuidaos=VGroup(texttuidao2,textn_1,textn_2)
        self.play(ReplacementTransform(texttuidaos,textntran));self.play(FadeOut(brace01),run_time=1.5)
        self.wait(1.5)
        #making line
        line1 = Line(textntran.get_edge_center(LEFT),texttuidao[2].get_edge_center(RIGHT),stroke_width=1.2)
        line2 = Line(textntran.get_edge_center(LEFT),np.array([-0.78,-1.95,0]),stroke_width=1.2)
        line3 = Line(textntran.get_edge_center(LEFT),texttuidao[4].get_edge_center(RIGHT),stroke_width=1.2)
        line4 = Line(textntran.get_edge_center(LEFT),np.array([-0.78,-2.8,0]),stroke_width=1.2)
        line5 = Line(textntran.get_edge_center(LEFT),texttuidao[6].get_edge_center(RIGHT),stroke_width=1.2)
        lines = VGroup(line1,line2,line3,line4,line5)
        lines.scale(0.97)
        for i in range(5):
            self.play(ShowCreation(lines[i]),run_time=0.5)

        texsum = TexMobject("\\Rightarrow{D_{n}=(n-1)(D_{n-2}+D_{n-1})}",color=YELLOW)
        texsum.scale(0.56)
        texsum.next_to(textntran,RIGHT*0.5)
        self.wait(1)
        self.play(Write(texsum))
        self.wait(5)
        
class cuopai_gs(Scene):
    def construct(self):        
        texsum2 = TexMobject("{D_{n}=(n-1)(D_{n-1}+D_{n-2})}\,(n\\geq3)",color=RED)
        texfromula01 = TextMobject("设$D_{n}=n!M_{n}$","易知$D_{1}=0,D_{2}=1$","\\ 则$M_{1}=0,M_{2}=\\frac{1}{2}$")
        texfromula01[0].set_color(ORANGE)
        texfromula02 = TexMobject("n!M_{n}","=","(n-1)(n-1)!M_{n-1}+(n-1)\\times(n-2)!M_{n-2}")
                                    
        texfromula03 = TexMobject("=","n!M_{n-1}-(n-1)!M_{n-1}+(n-1)!M_{n-2}")
        texsum2.scale(0.5);texsum2.to_corner(UL);texsum2.shift(UP*0.18+LEFT*0.1)
        texsum2.bg=SurroundingRectangle(texsum2,color=WHITE,buff=0.1);texsum2.bg.set_stroke(width=1.8)
        texfromula01.scale(0.56);texfromula01.to_edge(UP);texfromula01.shift(DOWN*0.45)
        texfromula02.scale(0.56);texfromula03.scale(0.56)
        texfromula02.next_to(texfromula01,DOWN);texfromula02.shift(LEFT*2.85);texfromula03.next_to(texfromula02,RIGHT)

        texfromula04 = TexMobject("nM_{n}-nM_{n-1}=-M_{n-1}+M_{n-2}")
        texfromula04.scale(0.56);texfromula04.next_to(texfromula01,DOWN);texfromula04.shift(DOWN*0.66)

        texfromula05 = TexMobject("M_{n}-M_{n-1}=-\\frac{1}{n}(M_{n-1}-M_{n-2})=",
                "(-\\frac{1}{n})(-\\frac{1}{n-1})\\dots(-\\frac{1}{3})(M_{2}-M_{1})=","(-1)^n\\frac{1}{n!}")
        texfromula05.scale(0.56);texfromula05.next_to(texfromula04,DOWN*0.9)

        texfromula06 = TexMobject("M_{n}-M_{n-1}","=","(-1)^n\\frac{1}{n!}")
        texfromula06.scale(0.56);texfromula06.next_to(texfromula05,DOWN*0.9)

        texfromula07 = TexMobject("M_{n-1}-M_{n-2}","=","(-1)^{(n-1)}}\\frac{1}{(n-1)!}")
        texfromula07.scale(0.56);texfromula07.next_to(texfromula06[1],DOWN*2.4,submobject_to_align=texfromula07[1])

        texfromula08 = TexMobject("\\dots","=","\\dots")
        texfromula08.scale(0.56);texfromula08.next_to(texfromula07[1],DOWN*1.8,submobject_to_align=texfromula08[1])
        texfromula08[2].next_to(texfromula08[1],RIGHT)
        texfromula08[0].next_to(texfromula08[1],LEFT)

        texfromula09 = TexMobject("M_{2}-M_{1}","=","(-1)^2\\frac{1}{2!}")
        texfromula09.scale(0.56);texfromula09.next_to(texfromula08[1],DOWN*1.8,submobject_to_align=texfromula09[1])

        texfromula10 = TexMobject("M_{n}","=","(-1)^2\\frac{1}{2!}+(-1)^3\\frac{1}{3!}+\\dots+(-1)^n\\frac{1}{n!}")
        texfromula10.scale(0.52);texfromula10.next_to(texfromula09,DOWN*0.8)

        texfromula11 = TexMobject("D_{n}=n!M_{n}","=","n!\\begin{bmatrix}\\frac{1}{2!}-\\frac{1}{3!}+\\dots+(-1)^n\\frac{1}{n!}\\end{bmatrix}",color=YELLOW)
        texfromula11.scale(0.65);texfromula11.next_to(texfromula10,1.1*DOWN)

        #animation
        self.play(Write(texsum2));self.play(ShowCreation(texsum2.bg),run_time=1.5)
        self.wait()
        for i in range(3):
            self.play(Write(texfromula01[i]));self.wait(1)
        self.play(Write(texfromula02[0:2]));self.wait(1)
        self.play(Write(texfromula02[2]));self.wait(1.8)
        self.play(Write(texfromula03));self.wait(1.8)
        self.play(FadeOut(texfromula02[1:3]))
        self.wait()
        self.play(ApplyMethod(texfromula03.next_to,texfromula02[0],RIGHT*0.7))
        self.wait()
        texgroup = VGroup(texfromula02[0],texfromula03)
        self.play(texgroup.shift,RIGHT*(texfromula01.get_center()[0]-texgroup.get_center()[0]))
        self.wait()
        self.play(Write(texfromula04))
        self.wait()
        self.play(Write(texfromula05[0]))
        self.wait()
        self.play(Write(texfromula05[1]))
        self.wait()
        self.play(Write(texfromula05[2]))
        self.wait(1.5)
        self.play(Write(texfromula06))
        self.wait()
        self.play(Write(texfromula07))
        self.wait()
        self.play(Write(texfromula08))
        self.wait()
        self.play(Write(texfromula09))      
        self.wait()
        self.play(Write(texfromula10))
        self.wait()
        self.play(Write(texfromula11))         
        self.wait(5)

class cuopai_gslst(Scene):
    def construct(self):
        self.wait(0.5)
        texsum3 = TexMobject("D_{n}","=","n!\\begin{bmatrix}\\frac{1}{2!}-\\frac{1}{3!}+\\dots+(-1)^n\\frac{1}{n!}\\end{bmatrix}",color=RED)
        texsum3.scale(0.6)
        texsum3.to_corner(UL)
        texsum3.bg = SurroundingRectangle(texsum3,color=WHITE,buff=0.1)
        texsum3.bg.set_stroke(width=1.8)
        texs1 = TexMobject("e^x=1+x+\\frac{x^2}{2!}+\\frac{x^3}{3!}+\\dots+\\frac{x^n}{n!}")
        texs1.scale(0.8)
        texs1.shift(UP*2)


        self.play(Write(texsum3));self.wait(0.5);self.play(ShowCreation(texsum3.bg))
        self.wait(1)
        self.play(Write(texs1))
        self.wait()
        tex1_1= TexMobject("-1",color=RED);tex1_1.scale(0.33);tex1_5 = TexMobject("(-1)",color=RED).scale(0.4)
        tex1_1.move_to(texs1[0][1]);tex1_5.move_to(texs1[0][5])
        
        texs1_m = TexMobject("(-1)",color=RED).scale(0.4)
        #debugTex(self,texs1[0])
        
        self.play(ReplacementTransform(texs1[0][1],tex1_1),ReplacementTransform(texs1[0][5],tex1_5),
                            *[ReplacementTransform(texs1[0][i],
                             texs1_m.copy().move_to(texs1[0][i].get_edge_center(DOWN))) for i in [7,13,23]],
                             run_time=1.6)
        self.wait()
        lasttex = TexMobject("D_{n}=n!e^{-1}=\\frac{n!}{e}")
        lasttex.scale(1)
        self.play(Write(lasttex))
        self.wait(3)

