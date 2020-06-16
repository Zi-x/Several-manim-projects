from manimlib.imports import *
from e_angle import *
import math
from Random_animation import *
class CodeLine(Text):
    CONFIG = {
        't2c': {
            '0.': ORANGE,
            '1.': ORANGE,
            '2.': ORANGE,
            '3.': ORANGE,
            '4.': ORANGE,
            '5.': ORANGE,
            '6.': ORANGE,
            '7.': ORANGE,
            '可视化':BLUE,
            '七大性质':RED,
            '(/≧▽≦/)':"#FF1493",
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': BLACK,
        'plot_depth': 2,
    }
class linear(Scene):
    CONFIG={
        "camera_config": {
        "background_color":WHITE ,#FFE4C4"
        }
    }
    def construct(self):
        grid = NumberPlane(
            
            center_point = LEFT*3,
            x_max = FRAME_X_RADIUS+6+6 +6,
            y_min = -6 -6, y_max = 6 +6,
            axis_config ={
            "stroke_color": BLACK,
            },
            number_line_config={
            "unit_size" : 0.8
            }
            ,plot_depth=-5                       
        )
         
        bg_ur = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color="#EBEBEB", fill_opacity=0.8848, plot_depth=-1)
        bg_ur.set_height(7.2, stretch=True).set_width(4.8, stretch=True)
        loc = UP * 1.325 + RIGHT * 4.5
        bg_ur.to_corner(RIGHT*0.48 + UP  )
        text01 = TexMobject(r"\begin{vmatrix} a_{11}&a_{12} \\a_{21}&a_{22}\end{vmatrix}",r"=",r"A",background_stroke_width=0,color = BLACK).set_stroke(width=0.7).move_to(loc)
        
        #making transform object
        point_texta11a12 = VGroup(text01[0][4:10]).set_color(RED).set_stroke(width=0.7).set_background_stroke(width=0)
        point_a11a12 = Dot(grid.c2p(1,3),color=BLACK).scale(0.7)
        point_texta21a22 = VGroup(text01[0][10:16]).set_color(GREEN).set_stroke(width=0.7).set_background_stroke(width=0)
        point_a21a22 = Dot(grid.c2p(4,1),color=BLACK).scale(0.7)

        ###
        point_a11 = VGroup(text01[0][4:7])
        point_a12 = VGroup(text01[0][7:10])
        point_a21 = VGroup(text01[0][10:13])
        point_a22 = VGroup(text01[0][13:16])
        ###

        arrow_red = Arrow(grid.c2p(0,0),point_a11a12.get_center(),buff=0,stroke_width=4.5,color=RED,plot_depth=-1.18)
        arrow_green = Arrow(grid.c2p(0,0),point_a21a22.get_center(),buff=0,stroke_width=4.5,color=GREEN,plot_depth=-1.18)

        vect_lab1 = TexMobject("l",color=BLACK).scale(0.7).move_to(arrow_red).shift(DOWN*0.1+RIGHT*0.15)
        vect_lab2 = TexMobject("m",color=BLACK).scale(0.7).move_to(arrow_green).shift(UP*0.16)
        
        jiaob = Arc(start_angle=14/180*PI,angle=-14/180*PI,radius=1.5,arc_center=grid.c2p(0,0),color=GREEN)
        arcb = VMobject()\
            .set_points_as_corners(
                [grid.c2p(0,0)]+[[1.5*np.cos(i/180*PI)+grid.c2p(0,0)[0],1.5*np.sin(i/180*PI),0] for i in range(14,-1,-1)]
            ).set_fill(color=GREEN,opacity=0.5).set_stroke(width=0)
        angleb=VGroup(arcb,jiaob)
        anglea = Angle(grid.c2p(1,0),grid.c2p(0,0),arrow_red.get_center(),color=RED,radius=0.5,stroke_width=4)
        
        anglea_lab  = TexMobject("\\alpha",color = RED,background_stroke_color=RED).scale(0.66)
        angleb_lab  = TexMobject("\\beta",color = GREEN,background_stroke_color=GREEN).scale(0.66)
        anglea_lab.next_to(anglea,RIGHT).shift(UP*0.25+LEFT*0.25)
        angleb_lab.next_to(jiaob,RIGHT*0.9).shift(UP*0.05)

        po1 = Polygon(grid.c2p(0,0),point_a11a12.get_center(),point_a11a12.get_center()+point_a21a22.get_center()-grid.c2p(0,0),point_a21a22.get_center(),plot_depth=-1.2)
        po1.set_fill(color=YELLOW,opacity=0.8).set_stroke(width=0,color=YELLOW)

        pocopy  =  po1.copy().set_fill(opacity=0).set_stroke(width=2.5,color=GOLD)
        po1copy = DashedVMobject(pocopy)
        #making formula texmobject
        formula01 = TexMobject("S","=","lm\\sin(\\beta-\\alpha)",color = BLACK,background_stroke_color=BLACK).scale(0.533)
        formula02 = TexMobject("=","lm(\\sin\\beta\\cos\\alpha-\\cos\\beta\\sin\\alpha)",color = BLACK,background_stroke_color=BLACK).scale(0.533)
        formula03 = TexMobject("=","(l\\cos\\alpha)m\\sin\\beta-(l\\sin\\alpha)m\\cos\\beta",color = BLACK,background_stroke_color=BLACK).scale(0.533)
        formula04 = TexMobject("=","a_{11}a_{22}-a_{12}a_{21}",color = BLACK,background_stroke_color=BLACK).scale(0.533)

        #COLOR
        formula01[0][0].set_color(YELLOW_D).set_stroke(width=1).set_background_stroke(color=YELLOW_D)

        formula01.next_to(text01,DOWN,aligned_edge=LEFT).shift(DOWN*0.88+LEFT*0.592)####################################################
        formula02.next_to(formula01[1],DOWN*1.7,submobject_to_align=formula02[0])
        formula03.next_to(formula02[0],DOWN*1.7,submobject_to_align=formula03[0])
        formula04.next_to(formula03[0],DOWN*1.7,submobject_to_align=formula04[0])
        formulas1 = VGroup(formula01,formula02,formula03,formula04)
        formula_greens = VGroup(formula01[2][6],formula02[1][6],formula02[1][15],formula03[1][11],formula03[1][24]).set_color(GREEN).set_background_stroke(color=GREEN)
        formula_redds  = VGroup(formula01[2][8],formula02[1][10],formula02[1][19],formula03[1][5],formula03[1][18]).set_color(RED).set_background_stroke(color=RED)

        texttip01 = TextMobject("即为二阶行列式的计算式","$\\alpha$为第一行向量与x轴正方向夹角",color = DARK_GRAY ,background_stroke_color = DARK_GRAY ).scale(0.45)
        texttip02 = TextMobject("$\\beta$为第二行向量与x轴正方向夹角",color = DARK_GRAY ,background_stroke_color = DARK_GRAY ).scale(0.45)
        greenvgroup = VGroup(texttip02[0][0]).set_color(GREEN).set_background_stroke(color=GREEN)
        redvgroup = VGroup(texttip01[1][0]).set_color(RED).set_background_stroke(color=RED)
        texttip01[0].next_to(formula04,DOWN*1,aligned_edge=LEFT)
        texttip01[1].next_to(texttip01[0],DOWN*0.7,aligned_edge=LEFT)
        texttip02.next_to(texttip01[1],DOWN*0.7,aligned_edge=LEFT)
        ######making textitle textmobject  ②③④⑤⑥⑦⑧⑨⑩
        title_size = 0.56
        title00 = TextMobject("0.行列式的几何意义",color = BLACK,background_stroke_color=BLACK).scale(0.65)
        title01 = TextMobject("1.行列式转置后值不变",color = BLACK,background_stroke_color=BLACK).scale(title_size)
        title02 = TextMobject("2.行列式某两行（列）交换，","符号改变",color = BLACK,background_stroke_color=BLACK).scale(title_size)
        title02[1].next_to(title02[0],DOWN*0.77,aligned_edge=LEFT)

        title03 = TextMobject("3.行列式某一行（列）倍乘k，","行列式变成原来的k倍",color = BLACK,background_stroke_color=BLACK).scale(title_size)
        title03[1].next_to(title03[0],DOWN*0.77,aligned_edge=LEFT)

        title04 = TextMobject("4.行列式某一行（列）加上其它","一行（列）的倍数，值不变",color = BLACK,background_stroke_color=BLACK).scale(title_size)
        title04[1].next_to(title04[0],DOWN*0.77,aligned_edge=LEFT)

        title05 = TextMobject("5.行列式中某行（列）元素是两个","元素之和,则可拆成两个行列式",color = BLACK,background_stroke_color=BLACK).scale(title_size)
        title05[1].next_to(title05[0],DOWN*0.77,aligned_edge=LEFT)

        title06 = TextMobject("6.行列式某两行（列）成比例，","行列式为0",color = BLACK,background_stroke_color=BLACK).scale(title_size)
        title06[1].next_to(title06[0],DOWN*0.77,aligned_edge=LEFT)

        title07 = TextMobject("7.行列式某一行（列）为0，","行列式为0",color = BLACK,background_stroke_color=BLACK).scale(title_size)
        title07[1].next_to(title07[0],DOWN*0.77,aligned_edge=LEFT)

        

        titless = VGroup(title00,title01,title02,title03,title04,title05,title06,title07)
        title00.next_to(text01,UP,aligned_edge=LEFT).shift(LEFT*0.6+UP*0.44)

        title000 = TextMobject("0.行列式七个性质完\\textasciitilde",color = BLACK,background_stroke_color=BLACK).scale(0.65).move_to(title00,aligned_edge=LEFT)
        title000[0][0:2].set_color(ORANGE).set_background_stroke(color=ORANGE)

        for i in range(7):
            titless[1+i].move_to(title00,aligned_edge=UL).shift(UP*0.15)
        
        for i in range(8):
            titless[i][0][0:2].set_color(ORANGE).set_background_stroke(color=ORANGE)

        
        ##################################################################################################################################
        self.play(ShowCreation(grid))
        labels1 = grid.get_coordinate_labels(number_config = {"color" : BLACK});labels1.set_plot_depth(-1.35)
        self.play(DrawBorderThenFill(labels1))
        self.play(FadeInFromDown(bg_ur))
        self.play(WriteRandom(title00[0]),run_time=1.8)
        self.wait(0.5)
        self.play(Write(text01[0]))
        self.wait(0.8)
        tips_left1 = TextMobject("为了方便演示","此处设",color=DARKER_GRAY,background_stroke_color=DARKER_GRAY,plot_depth = 3).scale(0.54)
        tips_left2 = TexMobject("a_{11}=1,a_{12}=3","a_{21}=4,a_{22}=1",background_stroke_color=DARKER_GRAY,color=DARKER_GRAY,plot_depth = 3).scale(0.5)
        tips_left2[1].next_to(tips_left2[0],DOWN*0.7,aligned_edge=LEFT)
        tips_left2.next_to(tips_left1,DOWN*0.7,aligned_edge=LEFT)
        tips_lefts = VGroup(tips_left1,tips_left2)
        tips_lefts.to_corner(UL,buff=0.15)
        self.play(Write(tips_lefts[0][0]));self.play(Write(tips_lefts[0][1]));self.play(Write(tips_lefts[1]))
        self.wait(0.5)
        self.play(ShowPassingFlashAround(point_texta11a12,buff=0),run_time=0.95)
        self.play(TransformFromCopy(point_texta11a12,point_a11a12))
        self.wait()
        self.play(ShowPassingFlashAround(point_texta21a22,buff=0),run_time=0.95)
        self.play(TransformFromCopy(point_texta21a22,point_a21a22))
        self.wait()
        self.play(DrawBorderThenFill(arrow_red),point_a11a12.set_opacity,0)
        self.play(DrawBorderThenFill(arrow_green),point_a21a22.set_opacity,0)
        self.play(DrawBorderThenFill(po1))
        self.wait()
        self.play(Write(vect_lab1));self.play(Write(vect_lab2))
        self.play(ShowCreation(anglea));self.play(DrawBorderThenFill(anglea_lab))
        self.play(ShowCreation(angleb,ratio=0.9));self.play(DrawBorderThenFill(angleb_lab))
        for i in range(3):
            self.play(Write(formulas1[i]));self.wait(1.88)
        self.play(Write(formulas1[3]));self.wait(0.5);self.play(Write(text01[1:]));self.wait(0.5)
        self.play(Write(texttip01[0]));self.wait(1)
        self.play(Write(texttip01[1]));self.wait(0.8);self.play(Write(texttip02));self.wait(0.5)
        self.wait()

        self.play(FadeOutRandom(title00[0]),run_time=1.5)
        self.play(Write(title01),run_time=1.5)
        self.play(FadeOut(vect_lab1),FadeOut(vect_lab2))
        angle_labouts = VGroup(anglea_lab,angleb_lab) ; angle_outs = VGroup(anglea,angleb)
        self.play(FadeOut(angle_labouts),FadeOut(angle_outs))
        self.wait(0.25)
        ########UPDATEAR#############
        arrow_green.add_updater(lambda d : d.put_start_and_end_on(grid.c2p(0,0),point_a21a22.get_center()))
        arrow_red.add_updater(lambda d : d.put_start_and_end_on(grid.c2p(0,0),point_a11a12.get_center()))
        po1.add_updater(lambda d: d.set_points_as_corners([grid.c2p(0,0)]+[point_a11a12.get_center()]+
                        [point_a11a12.get_center()+point_a21a22.get_center()-grid.c2p(0,0)]+[point_a21a22.get_center()]))
        #############################
            
        self.play(FadeIn(po1copy,run_time=0.1),point_a11a12.move_to,grid.c2p(1,4),point_a12.move_to,point_a21.get_center(),point_a12.set_color,GREEN,
                    point_a21a22.move_to,grid.c2p(3,1),point_a21.move_to,point_a12.get_center(),point_a21.set_color,RED,run_time=4.2)
        self.wait(1)
        
        self.play(FadeOut(po1copy,run_time=0.25),point_a11a12.move_to,grid.c2p(1,3),point_a12.move_to,point_a21.get_center(),point_a12.set_color,RED,
                        point_a21a22.move_to,grid.c2p(4,1),point_a21.move_to,point_a12.get_center(),point_a21.set_color,GREEN,run_time=4.2)
        self.wait()

        self.play(Transform(title01,title02,run_time=1.5))
        ###
        A_negative = TexMobject("-A",background_stroke_width=0,color = BLACK).scale(0.95).set_stroke(width=0.7).move_to(text01[2].get_center()).shift(RIGHT*0.12)
        A_negative[0][0].set_color(RED_D)
        AAA = TexMobject("A",background_stroke_width=0,color = BLACK).scale(0.95).set_stroke(width=0.7).move_to(text01[2].get_center())
        ###
        self.play(ReplacementTransform(text01[2],A_negative),point_a11a12.move_to,grid.c2p(4,1),point_texta11a12.move_to,point_texta21a22.get_center(),
                    point_a21a22.move_to,grid.c2p(1,3),point_texta21a22.move_to,point_texta11a12.get_center(),run_time=5)
        self.wait(0.5)
        self.play(ReplacementTransform(A_negative,AAA),point_a11a12.move_to,grid.c2p(1,3),point_texta11a12.move_to,point_texta21a22.get_center(),
                    point_a21a22.move_to,grid.c2p(4,1),point_texta21a22.move_to,point_texta11a12.get_center(),run_time=5)
        self.wait()
        ###
        k1 =  DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK).scale(0.45);k1copy = DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK).scale(0.45)
        k2 =  DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK).scale(0.45);k2copy =  DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK).scale(0.45)
        k1disp =  DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK).scale(0.45);k2disp =  DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK).scale(0.45)
        k1.move_to(point_a11.get_center()).shift(LEFT*0.535+UP*0.03);k1copy.move_to(point_a12.get_center()).shift(LEFT*0.535+UP*0.03)
        k2.move_to(point_a21.get_center()).shift(LEFT*0.535+UP*0.03);k2copy.move_to(point_a22.get_center()).shift(LEFT*0.535+UP*0.03)
        k1disp.move_to(AAA.get_center()).shift(RIGHT*0.042);k2disp.move_to(AAA.get_center()).shift(RIGHT*0.042)
        
        k1.add_updater(lambda d: d.set_value(grid.p2c(point_a11a12.get_center())[0]/1))
        k1copy.add_updater(lambda d: d.set_value(grid.p2c(point_a11a12.get_center())[0]/1))
        k1disp.add_updater(lambda d: d.set_value(grid.p2c(point_a11a12.get_center())[0]/1))

        k2.add_updater(lambda d: d.set_value(grid.p2c(point_a21a22.get_center())[0]/4))
        k2copy.add_updater(lambda d: d.set_value(grid.p2c(point_a21a22.get_center())[0]/4))
        k2disp.add_updater(lambda d: d.set_value(grid.p2c(point_a21a22.get_center())[0]/4))
        ###


        self.play(Transform(title01,title03,run_time=1.5))
        self.play(text01[0][0:4].shift,LEFT*0.5,AAA.shift,RIGHT*0.4)
        fadeoigroupk1s = VGroup(k1,k1copy,k1disp)
        fadeoigroupk2s = VGroup(k2,k2copy,k2disp)
        self.play(FadeIn(fadeoigroupk1s))
        self.play(FadeIn(po1copy),point_a11a12.move_to,grid.c2p(1.5,4.5),run_time=2.8);self.wait(0.6)
        self.play(point_a11a12.move_to,grid.c2p(-1.3,-3.9),run_time=4.8);self.wait()
        self.play(point_a11a12.move_to,grid.c2p(1,3),run_time=3.8)
        self.wait()
        self.play(FadeOut(fadeoigroupk1s),run_time=1.2)
        self.play(FadeIn(fadeoigroupk2s))
        self.play(point_a21a22.move_to,grid.c2p(8,2),run_time=3.8);self.wait(0.6)###############
        self.play(point_a21a22.move_to,grid.c2p(2,0.5),run_time=4);self.wait(2)
        self.play(FadeOut(po1copy),point_a21a22.move_to,grid.c2p(4,1),run_time=2.5)
        self.wait()

        self.play(Transform(title01,title04,run_time=1.5))
        self.wait(1.5)
        self.play(FadeOut(fadeoigroupk2s),text01[0][0:4].shift,RIGHT*0.5,AAA.shift,LEFT*0.4)
        #####
         
        A_eq_vgroup   =  VGroup(AAA,text01[1]);yuanlai_position_Aeq = A_eq_vgroup.get_center()
        position_Aeq = text01.get_edge_center(LEFT)-[0.05,1.03,0]#############################
        k3 =  DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK,include_sign=True).scale(0.45)       
        k4 =  DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK,include_sign=True).scale(0.45)
        
        
        textcopy_a11 = TexMobject("a_{11}",color=RED,background_stroke_color=RED).scale(0.65)
        textcopy_a12 = TexMobject("a_{12}",color=RED,background_stroke_color=RED).scale(0.65)
        #####
        self.wait(0.5)
        self.play(A_eq_vgroup.move_to,position_Aeq,point_a12.shift,RIGHT*0.75,point_a22.shift,RIGHT*0.75,
                    text01[0][16:20].shift,RIGHT*1.68)
        #########################
        k3.next_to(textcopy_a11,LEFT*0.24);k4.next_to(textcopy_a12,LEFT*0.24);textcopy_a11.shift(DOWN*0.02);textcopy_a12.shift(DOWN*0.02)
        k3_and_copy_a11 = VGroup(textcopy_a11,k3);k4_and_copy_a12 = VGroup(textcopy_a12,k4)
        k3_and_copy_a11.next_to(point_a21,RIGHT*0.36);k4_and_copy_a12.next_to(point_a22,RIGHT*0.36)

        k3.add_updater(lambda d: d.set_value((grid.p2c(point_a21a22.get_center())[0]-4)/1))
        k4.add_updater(lambda d: d.set_value((grid.p2c(point_a21a22.get_center())[0]-4)/1))
        ##########################
        self.play(Write(k3_and_copy_a11),Write(k4_and_copy_a12))
        self.wait(0.5)
        self.play(FadeIn(po1copy),point_a21a22.move_to,grid.c2p(4.3,1.9),run_time=3);self.wait(1.6)
        self.play(point_a21a22.move_to,grid.c2p(3,-2),run_time=4);self.wait(2)
        self.play(point_a21a22.move_to,grid.c2p(4,1),run_time=2.8);self.play(FadeOut(po1copy))
        self.wait()
        
        k1.clear_updaters();k1copy.clear_updaters(),k1disp.clear_updaters()
        k2.clear_updaters();k2copy.clear_updaters(),k2disp.clear_updaters()
        k3.clear_updaters();k4.clear_updaters()



        ###########
        c1tex = TexMobject("+\\,c_{1}",background_stroke_color=BLACK,color = BLACK).scale(0.58);c2tex = TexMobject("+\\,c_{2}",background_stroke_color=BLACK,color = BLACK).scale(0.58)
        c1change = TexMobject("+\\,1.0",background_stroke_color=BLACK,color = BLACK).scale(0.58);c2change = TexMobject("+\\,0.5",background_stroke_color=BLACK,color = BLACK).scale(0.58)
        c1tex.move_to(k3_and_copy_a11).shift(LEFT*0.06);c2tex.move_to(k4_and_copy_a12).shift(LEFT*0.06)
        c1change.move_to(c1tex).shift(LEFT*0.06);c2change.move_to(c2tex).shift(LEFT*0.06)
        ###########
        self.play(Transform(title01,title05,run_time=1.5));self.play(FadeOut(k3_and_copy_a11),FadeOut(k4_and_copy_a12))
        self.wait(0.8)       
        self.play(Write(c1tex),Write(c2tex))
        self.wait()
        self.play(ReplacementTransform(c1tex,c1change),ReplacementTransform(c2tex,c2change))
        self.wait(0.5)
        self.play(point_a21a22.move_to,grid.c2p(5,1.5));self.play(FadeOut(AAA))
        self.wait()
        #######
        text02 = TexMobject(r"\begin{vmatrix} a_{11}&a_{12} \\a_{21}&a_{22}\end{vmatrix}",background_stroke_width=0,color = BLACK).scale(0.488).set_stroke(width=0.7)
        text03 = TexMobject(r"\begin{vmatrix} a_{11}&a_{12} \\1.0&0.5\end{vmatrix}",background_stroke_width=0,color = BLACK).scale(0.488).set_stroke(width=0.7)
        texadd = TexMobject("+",background_stroke_width=0,color = BLACK).scale(0.5)
        text02.next_to(texadd,LEFT);text03.next_to(texadd,RIGHT)
        text2_3 = VGroup(text02,texadd,text03).next_to(text01[1],RIGHT)
        RED_text02 = VGroup(text02[0][4:10]).set_color(RED).set_stroke(width=0.7).set_background_stroke(width=0)
        GREEN_text02 = VGroup(text02[0][10:16]).set_color(GREEN).set_stroke(width=0.7).set_background_stroke(width=0)

        RED_text03 = VGroup(text03[0][4:10]).set_color(RED).set_stroke(width=0.7).set_background_stroke(width=0)
        

        po2 = Polygon(grid.c2p(0,0),grid.c2p(1,3),grid.c2p(5,4),grid.c2p(4,1),plot_depth=-1)
        po2.set_fill(color=YELLOW,opacity=0.8).set_stroke(width=0,color=YELLOW)
        po3 = Polygon(grid.c2p(0,0),grid.c2p(1,3),grid.c2p(2,3.5),grid.c2p(1,0.5),plot_depth=-1)
        po3.set_fill(color=YELLOW,opacity=0.8).set_stroke(width=0,color=YELLOW)

        po2copy_  =  po2.copy().set_fill(opacity=0).set_stroke(width=2.5,color=GOLD)
        po2copy = DashedVMobject(po2copy_)
        po3copy_  =  po3.copy().set_fill(opacity=0).set_stroke(width=2.5,color=ORANGE)
        po3copy = DashedVMobject(po3copy_)
        
        
        po4flash = Polygon(grid.c2p(0,0),grid.c2p(5,1.5),grid.c2p(4,1),plot_depth=-1)
        po4flash.set_fill(opacity=0).set_stroke(width=2.5,color=PINK)
        po5flash = Polygon(grid.c2p(1,3),grid.c2p(6,4.5),grid.c2p(5,4),plot_depth=-1)
        po5flash.set_fill(opacity=0).set_stroke(width=2.5,color=PINK)
        #######
        self.play(Write(text2_3))
        self.wait(0.8)
        self.play(TransformFromCopy(text02,po2copy))
        self.wait(0.5)
        self.play(TransformFromCopy(text03,po3copy))
        self.wait()
        self.play(po3copy.move_to,grid.c2p(4,1),{"aligned_edge":DL},run_time=2.4)
        self.wait(0.5)
        self.play(ShowCreationThenDestruction(po4flash),ShowCreationThenDestruction(po5flash),run_time=1.5)
        self.wait(0.8)
        self.play(ShowPassingFlashAround(c1change[0][1:4]),ShowPassingFlashAround(c2change[0][1:4]),
                        ShowPassingFlashAround(text03[0][10:13]),ShowPassingFlashAround(text03[0][13:16]),run_time=1.8)
        self.wait(1.5)
        
        self.play(FadeOut(po2copy),FadeOut(po3copy))
        self.play(FadeOut(text2_3),FadeIn(AAA),FadeOut(c1change),FadeOut(c2change))
        self.play(point_a21a22.move_to,grid.c2p(4,1),point_a12.shift,LEFT*0.75,point_a22.shift,LEFT*0.75,
                    text01[0][16:20].shift,LEFT*1.68,A_eq_vgroup.move_to,yuanlai_position_Aeq)
        #
        kk1 = DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK,include_sign=True).scale(0.44)       
        kk2 =  DecimalNumber(1,num_decimal_places=1,edge_to_fix=RIGHT,color=BLACK,include_sign=True).scale(0.44)
        kk1_right = TexMobject("a_{11}",color=RED,background_stroke_color=RED).scale(0.63)
        kk2_right = TexMobject("a_{12}",color=RED,background_stroke_color=RED).scale(0.63)
        kk1.next_to(kk1_right,LEFT*0.12)
        kk1vg = VGroup(kk1,kk1_right)
        kk2.next_to(kk2_right,LEFT*0.12)
        kk2vg = VGroup(kk2,kk2_right)
        kk1vg.move_to(point_a21).shift(RIGHT*0.0245);kk2vg.move_to(point_a22).shift(LEFT*0.016)
        
        point_a21_copy = point_a21.copy().move_to(point_a21)#############################################
        point_a22_copy = point_a22.copy().move_to(point_a22)#############################################
        point_a21_copy2 = point_a21.copy().move_to(point_a21)#############################################
        point_a22_copy2 = point_a22.copy().move_to(point_a22)#############################################

        number0_1 = TexMobject("0",color=BLACK,background_stroke_color=BLACK).move_to(AAA).shift(DOWN*0.05)
        number0_2 = TexMobject("0",color=BLACK,background_stroke_color=BLACK).move_to(AAA).shift(DOWN*0.05)
        AAA2  = AAA.copy().move_to(AAA)
        AAA3  = AAA.copy().move_to(AAA)
        
        #
        self.wait(0.5)
        self.play(Transform(title01,title06))
        self.wait()
        self.play(point_a21a22.move_to,grid.c2p(1,3),ReplacementTransform(point_a21,kk1vg),ReplacementTransform(point_a22,kk2vg),ReplacementTransform(AAA,number0_1),run_time=2.8)
        self.wait()
        ##
        kk1.add_updater(lambda d: d.set_value((grid.p2c(point_a21a22.get_center())[1])/3))
        kk2.add_updater(lambda d: d.set_value((grid.p2c(point_a21a22.get_center())[1])/3))
        ##
        self.play(point_a21a22.move_to,grid.c2p(1.5,4.5));self.wait()
        self.play(point_a21a22.move_to,grid.c2p(-1.6,-4.8),run_time=2.5);self.wait()
        self.play(point_a21a22.move_to,grid.c2p(1,3),run_time=2)
        self.wait()
        kk1.clear_updaters();kk2.clear_updaters()
        self.play(point_a21a22.move_to,grid.c2p(4,1),ReplacementTransform(kk1vg,point_a21_copy),ReplacementTransform(kk2vg,point_a22_copy),ReplacementTransform(number0_1,AAA2))
        self.wait()
        self.play(Transform(title01,title07))
        self.wait()
        ##
        number0_3 = TexMobject("0",color=BLACK,background_stroke_color=BLACK).move_to(point_a21_copy)
        number0_4 = TexMobject("0",color=BLACK,background_stroke_color=BLACK).move_to(point_a22_copy)

        point_a11_copy = point_a11.copy().move_to(point_a11)#############################################
        point_a12_copy = point_a12.copy().move_to(point_a12)#############################################
        number0_5= TexMobject("0",color=BLACK,background_stroke_color=BLACK).move_to(point_a11_copy)
        number0_6 = TexMobject("0",color=BLACK,background_stroke_color=BLACK).move_to(point_a12_copy)
        ##
        self.play(ReplacementTransform(point_a21_copy,number0_3),ReplacementTransform(point_a22_copy,number0_4),
                    point_a21a22.move_to,grid.c2p(0,0.0001),ReplacementTransform(AAA2,number0_2),run_time=2.8)
        self.wait()
        self.play(ReplacementTransform(point_a11,number0_5),ReplacementTransform(point_a12,number0_6),
                    point_a11a12.move_to,grid.c2p(0,0.0001),run_time=2)
        self.wait(2)

        self.play(ReplacementTransform(number0_5,point_a11_copy),ReplacementTransform(number0_6,point_a12_copy),
                    point_a11a12.move_to,grid.c2p(1,3),
                    ReplacementTransform(number0_3,point_a21_copy2),ReplacementTransform(number0_4,point_a22_copy2),
                    point_a21a22.move_to,grid.c2p(4,1),
                    ReplacementTransform(number0_2,AAA3),Transform(title01,title000),run_time=2)

        self.wait(5)

class kaitou(Scene):
    CONFIG={
        "camera_config": {
        "background_color":WHITE ,#FFE4C4"
        }
    }
    def construct(self):
        texthead = [
            "本视频将用可视化的方式展示行列式的七大性质",
            "0.行列式的几何意义",
            "1.行列式转置后值不变",
            "2.行列式某两行（列）交换，符号改变",
            "4.行列式某一行（列）加上其它一行（列）的倍数，值不变",
            "5.行列式中某行（列）元素均是两个元素之和,则可拆成两个行列式",
            "6.行列式某两行（列）成比例，行列式为0",
            "7.行列式某一行（列）为0，行列式为0",        
        ]
        textheads = VGroup(
            *[
                CodeLine(cap, font='思源黑体', size=0.4).to_edge(UP*1.25)
                for cap in texthead
            ]
        )
        textheads[0].scale(1.5)
        textheads[2].next_to(textheads[1],RIGHT*8)
        texthead12 = VGroup(textheads[1],textheads[2]).next_to(textheads[0],DOWN*2.4)
        textheads[3].next_to(texthead12,DOWN*2.5)
        for i in range(3,7):
            textheads[i+1].next_to(textheads[i],DOWN*2.5)

        self.play(Write(textheads[0],run_time=2.4))
        self.wait()
        self.play(FadeInRandom(textheads[1:]),run_time=4.5)
        self.wait(2)
        self.play(FadeOutRandom(textheads[1:]),FadeOut(textheads[0]),run_time=2)
        self.wait()