from manimlib.imports import *
from e_angle import *
import math
class CodeLine(Text):
    CONFIG = {
        't2c': {
            '粉色':"#FF69B4",
            '(/≧▽≦/)':"#FF1493",
            'r': BLUE,
            'x':"#F39800",
            'y':"#F39800",
            'σ': TEAL,
            'D': BLUE,            
            '-r^2':"#F39800",     
            'θ':BLUE,
            'π':RED,
            '2π':"#F39800",
            '0':"#F39800",
            '+∞':"#F39800",  
            'dxdy': BLUE,
            'dθ': BLUE,
            'rdθ': BLUE,
            'dr': BLUE,
            'rdθdr': BLUE,
            'A^2':RED,
            '根号π' :RED,
            '∫' :RED,
            "整个平面":"#FF69B4",
            "长":YELLOW,
            "宽":GREEN_SCREEN,
            '反常积分':YELLOW,
            '经验归纳':ORANGE,
            '通式':RED,
            'x^2' :RED,
            'x^4' :RED,
            'x^2n' :RED,
            '-(x^2+y^2)':"#F39800",
            '0、' :WHITE,
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': WHITE,
        'plot_depth': 2,
    }
class int1(GraphScene):
    CONFIG={
        "camera_config": {
        "background_color":BLACK ,#"#FFE4C4"
        },
        "x_min":-4,
        "x_max":4,
        "y_min":0,
        "y_max":1.4,
        "x_axis_width": 12,
        "y_axis_height": 5,
        "graph_origin":[-0,-1.5,0],
        "function_color":RED,
        "y_tick_frequency": 3,
        "x_tick_frequency": 10,
        "axes_color":GREY,
        "x_labeled_nums":range(-3,4,1),
        "y_labeled_nums":[1],
        } 
    def construct(self):


        self.setup_axes(animate=True)
        func1 = self.get_graph(self.func_1,color=RED).set_stroke(width=3)
        func_lab1 = self.get_graph_label(func1,label="e^{-x^2}",color=ORANGE,x_val=1.4,direction=UP)
        func_lab1.shift(UP*2.8)


        rects =self.get_riemann_rectangles(func1,dx=0.24,x_min=-3,x_max=3,stroke_width=0,width_scale_factor=0.964)
        rects2 =self.get_riemann_rectangles(func1,dx=0.15,x_min=-3,x_max=3,stroke_width=0,width_scale_factor=0.955)
        rects3=self.get_riemann_rectangles(func1,dx=0.065,x_min=-3,x_max=3,stroke_width=0,width_scale_factor=0.984)
        rects4=self.get_riemann_rectangles(func1,dx=0.03,x_min=-3,x_max=3,stroke_width=0)
        rects5=self.get_riemann_rectangles(func1,dx=0.006,x_min=-3,x_max=3,stroke_width=0,width_scale_factor=1.9)
        


        rectvps = VGroup(rects,rects2,rects3,rects4,rects5)
        for i in range(5):
            rectvps[i].set_plot_depth(1)
            
        
        
        #########################################################################
        self.play(ShowCreation(func1))
        self.play(Write(func_lab1))
        '''
        self.play(ShowCreation(rects))
        self.transform_between_riemann_rects(rects,rects2)
        self.transform_between_riemann_rects(rects,rects3)        
        self.transform_between_riemann_rects(rects,rects4)'''
        self.transform_between_riemann_rects(rects,rects5)
    
        ###############
        tex01 = TexMobject("\\int_{-\\infty}^{+\\infty}e^{-x^2}dx",
                        color=YELLOW,plot_depth=2,background_stroke_width=0).scale(0.95).set_stroke(width=1.5).shift(LEFT*0.0425)
        ###############
        self.play(FadeOut(func_lab1),FadeIn(tex01,run_time=1.2))
        self.wait(2.5)
        '''
        self.play(FadeOut(self.axes),FadeOut(func1),FadeOut(rects))
        self.wait(0.5)
        self.play(tex01.to_corner,UL)
        self.wait(2)'''
        
    def func_1(self,x):
        return np.exp(-x*x)
    
class int2(Scene):
    def construct(self):
        tex01 = TexMobject("\\int_{-\\infty}^{+\\infty}e^{-x^2}dx",color=YELLOW,plot_depth=2,background_stroke_width=0).scale(0.9).set_stroke(width=0.6).to_corner(UL)
        tex02 = TexMobject("\\int_{-\\infty}^{+\\infty}e^{-y^2}dy",color=ORANGE,plot_depth=2,background_stroke_width=0).scale(0.9).set_stroke(width=0.6).to_corner(UR)

        tex03 = TexMobject("=","A^2")
        tex03[0].set_color(WHITE);tex03[1].set_color(RED).scale(1.08)
        
        #formu01 = TexMobject("\\int_{-\\infty}^{+\\infty}e^{-x^2}dx\\int_{-\\infty}^{+\\infty}e^{-y^2}dy").scale(0.9).to_edge(UP)
        
        tex01copy = tex01.copy().to_corner(UR)
        ############zimum########################################################
        textzimu = [
            "现在对此积分的值进行求解",
            "我们将其复制一份",
            "改变它的积分变量为y",
            "然后将它们相乘",
            "设相乘后值为A*A即为A^2",
            "将其合并，区域D为整个平面",
            "然后将其转换成极坐标系下形式",
            "其中-(x^2+y^2)=-r^2",
            "而dσ=dxdy变成dσ=rdθdr",
            "由于区域D为整个平面，所以r范围为0到+∞",            
            "θ范围为0到2π",                      
            "这时可能有人要问了，为什么dσ=rdθdr呢？",  #11
            "先画一个坐标系（以第一象限为例）",
            "然后以极坐标系的方式进行细分",
            "取其中一个dσ进行探究",
            "当足够细分时，dσ可以近似看作一个矩形",
            "矩形的长为rdθ",
            "矩形的宽为dr",
            "所以矩形的面积dσ为长乘宽，即rdθdr",   #18
            "接下来继续求解~(先算出∫dθ，再凑微分)",
            "于是可以解得A^2=π",
            "所以此积分的值为根号π"
        ]
        textzimus = VGroup(
            *[
                CodeLine(cap, font='思源黑体', size=0.32).to_edge(DOWN * 0.78)
                for cap in textzimu
            ]
        )
        #########################################
        tex04 = TexMobject("=","\\iint\\limits_{D}e^{-(x^2+y^2)}dxdy").scale(0.8).set_color("#F39800").set_stroke(width=0.5)#set_color()
        
        tex04[0][0].set_color(WHITE);tex04[1][1].set_color(BLUE);tex04[1][0].set_color(RED_D)
        tex04[1][11:15].set_color(BLUE)

        tex05 = TexMobject("=",
                "\\int_{0}^{2\\pi}\\int_{0}^{+\\infty}e^{-r^2}rd\\theta{dr}").scale(0.8).set_color("#F39800").set_stroke(width=0.5)
        tex05[0][0].set_color(WHITE)
        tex05_red_D = VGroup(tex05[1][0],tex05[1][4]).set_color(RED_D)
        tex05[1][12:17].set_color(BLUE)

        tex06 = TexMobject("=",
                "\\int_{0}^{2\\pi}d\\theta","\\int_{0}^{+\\infty}e^{-r^2}rdr").scale(0.8).set_color("#F39800").set_stroke(width=0.5)
        tex06[0][0].set_color(WHITE);tex06[1][0].set_color(RED_D);tex06[1][4:6].set_color(BLUE)
        tex06[2][0].set_color(RED_D);tex06[2][8:].set_color(BLUE)

        tex07 = TexMobject("=",
                "-\\pi","\\int_{0}^{-\\infty}e^{-r^2}{d(-r^2)}").scale(0.8).set_color("#F39800").set_stroke(width=0.5)
        tex07[0][0].set_color(WHITE);tex07[2][0].set_color(RED_D)
        tex07[2][8:14].set_color(BLUE)

        tex08 = TexMobject("=","\\pi",color=RED)
        tex08[0].set_color(WHITE)
        tex08[0].scale(0.8);tex08[1].scale(1.1)

        tex09 = TexMobject("\\int_{-\\infty}^{+\\infty}e^{-x^2}dx","=","\\sqrt{\\pi}").set_stroke(width=0.5).scale(0.78)
        tex09[1].set_color(WHITE);tex09[0].set_color(YELLOW);tex09[2].set_color(RED)
        tex09[2].scale(1.12)
        tex09[0].shift(RIGHT*4.25+0.2*UP)                    ###############################                                                       
        tex09[1].next_to(tex09[0],RIGHT);tex09[2].next_to(tex09[1],RIGHT)
        
        #########################################
                
        self.wait(0.5)
        self.add(tex01)
        self.play(Write(textzimus[0]))
        self.wait()
        self.play(ReplacementTransform(textzimus[0],textzimus[1]))
        self.play(TransformFromCopy(tex01,tex01copy))
        self.wait(1)
        self.play(ReplacementTransform(textzimus[1],textzimus[2]))
        self.play(ReplacementTransform(tex01copy,tex02))
        self.wait()
        self.play(ReplacementTransform(textzimus[2],textzimus[3]))
        self.play(tex01.shift,RIGHT*4.25,tex01.scale,0.77,tex02.shift,LEFT*4.25,tex02.scale,0.77)
        ############################
        tex03[0].next_to(tex01,LEFT);tex03[1].next_to(tex03[0],LEFT);tex03[1].shift(UP*0.06+LEFT*0.09)
        tex04.next_to(tex03[0],DOWN*4.8,submobject_to_align=tex04[0])
        tex05.next_to(tex04[0],DOWN*4.8,submobject_to_align=tex05[0])
        tex06.next_to(tex05[0],DOWN*4.8,submobject_to_align=tex06[0])
        tex07.next_to(tex06[0],DOWN*4.8,submobject_to_align=tex07[0])
        tex08[0].next_to(tex07[2],RIGHT*1.2)
        tex08[1].next_to(tex08[0],RIGHT*1.05)
        
        ############################
        self.wait()
        self.play(ReplacementTransform(textzimus[3],textzimus[4]))
        self.play(Write(tex03[0]));self.play(Write(tex03[1]))
        self.wait()
        self.play(ReplacementTransform(textzimus[4],textzimus[5]))
        self.play(Write(tex04))
        self.wait()
        self.play(ReplacementTransform(textzimus[5],textzimus[6]))
        
        vgt01 = VGroup(tex05[1][0],tex05[1][4],tex05[1][8])
        self.play(Write(tex05[0]));self.play(Write(vgt01))
        self.wait(0.6)
        self.play(ReplacementTransform(textzimus[6],textzimus[7]))
        vcopy01 = VGroup(tex04[1][3:11])
        vcopy02 = VGroup(tex05[1][9:12])
        self.wait(0.25);self.play(ShowPassingFlashAround(vcopy01,run_time=1))
        self.play(TransformFromCopy(vcopy01,vcopy02))
        self.wait(0.6)
        vcopy03 = VGroup(tex04[1][11:15])
        vcopy04 = VGroup(tex05[1][12:17])
        self.play(ReplacementTransform(textzimus[7],textzimus[8]))
        self.wait(0.25);self.play(ShowPassingFlashAround(vcopy03,run_time=1))
        self.play(TransformFromCopy(vcopy03,vcopy04))
        self.wait(1)
        
        self.play(ReplacementTransform(textzimus[8],textzimus[9]));self.wait(0.25)
        self.play(Write(tex05[1][7]));self.play(Write(tex05[1][5:7]))
        self.wait(0.6)
        self.play(ReplacementTransform(textzimus[9],textzimus[10]))
        self.play(Write(tex05[1][3]));self.play(Write(tex05[1][1:3]))
        self.wait(0.6)
        self.play(ReplacementTransform(textzimus[10],textzimus[11]))
        self.wait(2.5);self.play(ReplacementTransform(textzimus[11],textzimus[12]))

        ############making d6 object##############
        line01 = Line([-0.2,0,0],[2,0,0])
        line02 = Line([0,2,0],[0,-0.2,0])
        lineaxis = VGroup(line01,line02)
        lineaxis.shift(LEFT*5.6+DOWN*0.5)
        d1 = line_intersection(line01.get_start_and_end(),line02.get_start_and_end())
        arcs = VGroup()
        for i in range(10):
            arc_ = Arc(radius=(i+1)*0.18,start_angle=TAU/4,angle=-TAU/4,arc_center=d1,color=GREY)
            arc_.set_stroke(width=2.5)
            arcs.add(arc_)
        lines = VGroup()
        for i in range(1,10):
            line_ = Line(d1,d1+[2*np.cos(PI/2-i*PI/20),2*np.sin(PI/2-i*PI/20),0],color=GREY)
            line_.set_stroke(width=2.5)
            lines.add(line_)

        dd1 = Dot([d1+[0.18*6*np.cos(PI/2-4*PI/20),0.18*6*np.sin(PI/2-4*PI/20),0]])
        dd2 = Dot([d1+[0.18*6*np.cos(PI/2-5*PI/20),0.18*6*np.sin(PI/2-5*PI/20),0]]) 
        dd3 = Dot([d1+[0.18*7*np.cos(PI/2-5*PI/20),0.18*7*np.sin(PI/2-5*PI/20),0]])
        dd4 = Dot([d1+[0.18*7*np.cos(PI/2-4*PI/20),0.18*7*np.sin(PI/2-4*PI/20),0]])

        po1 = Polygon(dd1.get_center(),dd2.get_center(),dd3.get_center(),dd4.get_center(),plot_depth=-1).set_stroke(width=0).set_fill(color="#FF69B4",opacity=0.8)
        poline_length = Line(dd1.get_center(),dd2.get_center(),color=YELLOW,plot_depth=1).set_stroke(width=2.65)
        poline_width = Line(dd1.get_center(),dd4.get_center(),color=GREEN_SCREEN,plot_depth=0.5).set_stroke(width=2.65) 

        arrow1 = Arrow(start=poline_width.get_center()+[-1.3,0,0],end=poline_width.get_center(),
                    stroke_width=2.1,max_tip_length_to_length_ratio= 0.133,buff=0.065,color=LIGHT_GREY)
        arrow2 = Arrow(start=poline_length.get_center()+[0,-1.3,0],end=poline_length.get_center(),
                    stroke_width=2.1,max_tip_length_to_length_ratio= 0.133,buff=0.065,color=LIGHT_GREY)

        arrow1note = TexMobject("dr",color=BLUE).scale(0.6).next_to(arrow1,LEFT*0.5)
        arrow2note = TexMobject("rd\\theta",color=BLUE).scale(0.6).next_to(arrow2,DOWN*0.5)
        


        #################ANIMATION############################
        self.play(ShowCreation(lineaxis))        
        self.wait()
        self.play(ReplacementTransform(textzimus[12],textzimus[13]))
        
        self.play(ShowCreation(arcs,lag_ratio=1,run_time=3,rate_func=linear))
        self.play(ShowCreation(lines,lag_ratio=1,run_time=3,rate_func=linear))

        self.play(ReplacementTransform(textzimus[13],textzimus[14]));self.wait(0.2)
        self.play(ShowCreation(po1))
        self.wait(0.6)
        self.play(ReplacementTransform(textzimus[14],textzimus[15]))
        self.wait(1.8)
        self.play(ReplacementTransform(textzimus[15],textzimus[16]))
        self.play(ShowCreation(poline_length));self.play(ShowCreation(arrow2));self.play(Write(arrow2note))
        self.wait()
        self.play(ReplacementTransform(textzimus[16],textzimus[17]))
        self.play(ShowCreation(poline_width));self.play(ShowCreation(arrow1));self.play(Write(arrow1note))
        self.wait()
        self.play(ReplacementTransform(textzimus[17],textzimus[18]))
        self.wait(3)
        self.play(ReplacementTransform(textzimus[18],textzimus[19]))
        self.play(Write(tex06));self.wait(2);self.play(Write(tex07))
        self.wait(2.5)
        self.play(ReplacementTransform(textzimus[19],textzimus[20]))
        self.play(Write(tex08))
        self.wait()
        self.play(ReplacementTransform(textzimus[20],textzimus[21]))
        self.play(Write(tex09),run_time=1.5);self.wait(0.20);self.play(ShowPassingFlashAround(tex09,run_time=1.2))        
        self.wait(5)


class int3(GraphScene):
    CONFIG={
        "camera_config": {
        "background_color":BLACK ,#"#FFE4C4"
        },
        "x_min":-4,
        "x_max":4,
        "y_min":0,
        "y_max":1.2,
        "x_axis_width": 7.8,
        "y_axis_height": 2.7,
        "graph_origin":[-0,-1.5,0],
        "function_color":RED,
        "y_tick_frequency": 3,
        "x_tick_frequency": 20,
        "axes_color":GREY,
        "x_labeled_nums":range(-3,4,1),
        "y_labeled_nums":[1],
        "x_axis_label":None,       
        "y_axis_label":None,  
        } 
        
    def construct(self):
        textzimu = [
            "刚才我们已经求出此反常积分值为根号π",
            "但有时候题目往往在前面乘一个x^2n，(n为0、1、2、3...)",
            "这时反常积分的值又为多少呢？",
            "我们可以先算出乘x^2、x^4的情况",
            "然后进行经验归纳求其通式(略_(:з」∠)_)",
            "这便是此类反常积分的通式啦！(/≧▽≦/)",
            
        ]
        zimus = VGroup(
            *[
                CodeLine(cap, font='思源黑体', size=0.32).to_edge(DOWN * 0.78)
                for cap in textzimu
            ]
        )
        
        texup01 = TexMobject("\\int_{-\\infty}^{+\\infty}e^{-x^2}dx","=","\\sqrt{\\pi}").scale(0.76).set_stroke(width=0.3)
        texup01[1].set_color(WHITE);texup01[0].set_color(YELLOW);texup01[2].set_color(RED)

        texup02 = TexMobject("\\int_{-\\infty}^{+\\infty}x^2e^{-x^2}dx","=","\\frac{1}{2}\\sqrt{\\pi}").scale(0.75).set_stroke(width=0.3)
        texup02[1].set_color(WHITE);texup02[0].set_color(YELLOW);texup02[2].set_color(RED)

        texup03 = TexMobject("\\int_{-\\infty}^{+\\infty}x^4e^{-x^2}dx","=","\\frac{3}{4}\\sqrt{\\pi}").scale(0.75).set_stroke(width=0.3)
        texup03[1].set_color(WHITE);texup03[0].set_color(YELLOW);texup03[2].set_color(RED)

        texup04 = TexMobject("\\int_{-\\infty}^{+\\infty}x^6e^{-x^2}dx","=","\\frac{15}{8}\\sqrt{\\pi}").scale(0.75).set_stroke(width=0.3)
        texup04[1].set_color(WHITE);texup04[0].set_color(YELLOW);texup04[2].set_color(RED)

        textdots = TexMobject("\\dots")

        texup01.to_corner(UL,buff=0.55);texup02.next_to(texup01,RIGHT*2.5);texup03.next_to(texup02,RIGHT*2.5);textdots.next_to(texup03,RIGHT*1.25)

        textend = TexMobject("\\int_{-\\infty}^{+\\infty}x^{2n}e^{-x^2}dx","=","\\frac{(2n-1)!!}{2^n}\\sqrt{\\pi}").scale(1.1)
        textend[1].set_color(WHITE)
        textend[0].set_color(YELLOW)
        textend[2].set_color(RED)

          
        
        self.play(Write(texup01[0:2]))
        self.setup_axes(animate=True)
        #############################################################################################################
        func1 = self.get_graph(self.func_1,color=RED).set_stroke(width=3)
        func_lab1 = self.get_graph_label(func1,label="e^{-x^2}",color=ORANGE,x_val=1.8,direction=UP).scale(0.8).set_stroke(width=0.35)
        func_lab1.shift(UP*0.8)

        func2 = self.get_graph(self.func_2,color=RED).set_stroke(width=3)
        func_lab2 = self.get_graph_label(func2,label="x^2e^{-x^2}",color=ORANGE,x_val=1.8,direction=UP).scale(0.8).set_stroke(width=0.35)
        func_lab2.shift(UP*0.8)

        func3 = self.get_graph(self.func_3,color=RED).set_stroke(width=3)
        func_lab3 = self.get_graph_label(func3,label="x^4e^{-x^2}",color=ORANGE,x_val=1.8,direction=UP).scale(0.8).set_stroke(width=0.35)
        func_lab3.shift(UP*0.8)

        brect1=self.get_riemann_rectangles(func1,dx=0.005,x_min=-3,x_max=3,stroke_width=0,width_scale_factor=1.9)
        brect2=self.get_riemann_rectangles(func2,dx=0.005,x_min=-3,x_max=3,stroke_width=0,width_scale_factor=1.9)
        brect3=self.get_riemann_rectangles(func3,dx=0.005,x_min=-3,x_max=3,stroke_width=0,width_scale_factor=1.9)
        #############################################################################################################
        
        
        self.play(ShowCreation(func1))
        self.play(ShowCreation(brect1));self.play(Write(func_lab1))
        self.play(Write(zimus[0]))
        self.wait(0.2)
        self.play(Write(texup01[2]))
        self.wait(1.42)
        self.play(ReplacementTransform(zimus[0],zimus[1]))
        self.wait()
        self.play(Write(texup02[0:2]))
        self.wait(0.5)
        self.play(ReplacementTransform(func1,func2),ReplacementTransform(brect1,brect2),ReplacementTransform(func_lab1,func_lab2))
        self.wait()
        self.play(Write(texup03[0:2]))
        self.wait(0.5)
        self.play(ReplacementTransform(func2,func3),ReplacementTransform(brect2,brect3),ReplacementTransform(func_lab2,func_lab3))
        self.wait()
        self.play(Write(textdots));self.play(ReplacementTransform(zimus[1],zimus[2]))
        self.wait(1.6);self.play(ReplacementTransform(zimus[2],zimus[3]))
        self.play(Write(texup02[2]));self.wait(0.5);self.play(Write(texup03[2]))
        self.wait(1.2)
        self.play(ReplacementTransform(zimus[3],zimus[4]))
        self.wait(3)
        fadeoutVgroup = VGroup(textdots,texup01,texup02,texup03,func_lab3,brect3,func3)
        self.play(FadeIn(textend,run_time=1.6),FadeOut(fadeoutVgroup,run_time=1),FadeOut(self.axes,run_time=1),ReplacementTransform(zimus[4],zimus[5]))
        self.wait(6)
        

    

    def func_1(self,x):
        return np.exp(-x*x)
    
    def func_2(self,x):
        return x*x*np.exp(-x*x)
    
    def func_3(self,x):
        return x*x*x*x*np.exp(-x*x)
        
        

