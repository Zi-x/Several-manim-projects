from manimlib.imports import *
import math
class yuans(Scene):
    def construct(self):
        #making circle
        circle0 = Circle(radius=1.6,color=RED)
        #making shanxing
        arc00 = Arc(radius=1.6,angle=PI/10,color=RED)
        line00 = Line([0,0,0],[1.6194,0,0],color=RED)
        line01 = Line([0,0,0],[1.6185*np.cos(PI/10),1.6*np.sin(PI/10),0],color=RED)
        shanxing = VGroup(arc00,line00,line01)
        shanxing.rotate_about_origin(PI/2-PI/20)
        #making lines
        line0 = Line([-1.612,0,0],[1.612,0,0],color=RED,stroke=0.6)
        lines = VGroup()
        for i in range(10):
            lines_ = line0.copy().rotate_about_origin(i*PI/10)
            lines.add(lines_)
        #making shans
        shans = VGroup()
        for i in range(10):
            sahnxing_=shanxing.copy().shift((5-i)*1.6*LEFT*np.sin(PI/10))
            shans.add(sahnxing_)
        #making text
        text01 = TextMobject("有一半径为$r$","周长为$C$的圆")
        text02 = TexMobject("\\text{定义}\\pi=\\frac{C}{2r}")
        text03 = TextMobject("现将其沿圆心切割为$n$个扇形")
        text04 = TextMobject("展开两半扇形、","对准、","插入")
        text05 = TextMobject("得到一个平行四边形")
        text06 = TextMobject("当$n$趋向$\\infty$时","长为$\\frac{C}{2}$","高为$r$")
        text07 = TexMobject("S_{\\text{圆}}=\\pi{r^2}")
        text05ss = VGroup(text01,text02,text03,text04,text05,text06,text07)
        for i in range(6):
            text05ss[i].scale(0.556)
        text05ss[0].to_corner(UR)
        for i in range(1,6):
            text05ss[i].next_to(text05ss[i-1],DOWN)
        text07.scale(0.95);text07.next_to(text06,DOWN*2.5)
        #making tex
        texxxt1= TexMobject("S","=","\\frac{C}{2}\\times{r}")
        texxxt2= TexMobject("=","\\pi{r}\\times{r}")
        texxxt3= TexMobject("=","\\pi{r^2}")
        texxxt1.scale(0.8); texxxt2.scale(0.8); texxxt3.scale(0.8)
        
        texxxt1.to_corner(UL);texxxt1.shift(RIGHT*0.25)
        texxxt2.next_to(texxxt1[1],3*DOWN,submobject_to_align=texxxt2[0])
        texxxt3.next_to(texxxt2[0],3*DOWN,submobject_to_align=texxxt3[0])
        texxxs = VGroup(texxxt1,texxxt2,texxxt3)

        
        #position
        shans.shift(UP);shans2=shans.copy().rotate_about_origin(PI)
        shans.shift(DOWN+RIGHT*1.6*np.sin(PI/20));shans2.shift(UP+LEFT*1.6*np.sin(PI/20))
        #ⅠⅢⅥⅣⅤⅦⅧⅨⅩⅪⅫ
        textq = TexMobject("\\text{前置知识}1—\\text{圆面积推导}")
        textq.scale(1.8)
        self.play(FadeIn(textq))
        self.wait(1.66)
        self.play(FadeOut(textq))
        self.play(Write(text05ss[0][0]),run_time=1.5);self.wait(0.5);self.play(Write(text05ss[0][1]),run_time=1.2)
        self.play(ShowCreation(circle0))
        self.play(Write(text05ss[1]),run_time=1.8)
        self.wait(0.5)
        self.play(ShowCreation(lines[0]))
        self.play(Write(text05ss[2]))
        for i in range(1,10):
            self.play(ShowCreation(lines[i]))
        lineandcircle = VGroup(lines,circle0)
        shansss       = VGroup(shans,shans2)
        
        self.wait(1.6)
        self.play(FadeOut(lineandcircle,run_time=1),FadeIn(shansss,run_time=1.8),Write(text05ss[3][0]))
        self.wait()
        self.play(ApplyMethod(shans.shift,LEFT*1.6*np.sin(PI/20)),Write(text05ss[3][1]))
        self.wait(0.5)
        self.play(ApplyMethod(shans.shift,DOWN*1.6),Write(text05ss[3][2]))
        self.wait(0.5)
        self.play(Write(text05ss[4]),ApplyMethod(shansss.shift,UP*1.2+LEFT*0.32))
        self.wait(0.85)
        self.play(Write(text05ss[5][0]));self.wait(0.65);self.play(Write(text05ss[5][1]));self.wait(0.5);self.play(Write(text05ss[5][2]))
        self.wait(1.2)
        self.play(Write(texxxs[0]));self.wait(0.6);self.play(Write(texxxs[1]));self.wait(0.6);self.play(Write(texxxs[2]))
        self.wait(1.2)
        self.play(Write(text07))
        self.wait(5)



class lengzhui(ThreeDScene):
    def construct(self):
        #kaitou
        textq = TexMobject("\\text{前置知识}2—\\text{棱锥体积推导}")
        textq.scale(1.8)
        self.play(FadeIn(textq))
        self.wait(1.6)
        self.play(FadeOut(textq))
        self.wait(0.5)
        
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        #棱柱
        facebians_=VGroup()
        face1 = Polygon([2,0,0],[-2*np.cos(PI/3),2*np.sin(PI/3),0],[-2*np.cos(PI/3),-2*np.sin(PI/3),0])
        verts1=face1.get_vertices()
        face2= face1.copy().shift(OUT*2.5)
        verts2=face2.get_vertices();face_xs = VGroup(face1,face2)
        for i in range(3):
            if i == 2:
                facebian = Polygon(verts1[i],verts2[i],verts2[0],verts1[0])
            else:
                facebian = Polygon(verts1[i],verts2[i],verts2[i+1],verts1[i+1])
            facebian.set_stroke(width=1,color=BLUE)
            facebian.set_fill(color=BLUE,opacity=0.7)
            facebians_.add(facebian)
        face1.set_stroke(width=1,color=BLUE);face1.set_fill(color=BLUE,opacity=0.7)
        face2.set_stroke(width=1,color=BLUE);face2.set_fill(color=BLUE,opacity=0.7)
        #text
        text01 = TexMobject("\\because\,V_{\\text{红}}","=","V_{\\text{绿}}")
        text01[0].set_color(ORANGE);text01[2].set_color(GREEN)
        text02 = TexMobject("\\because\,V_{\\text{黄}}","=","V_{\\text{绿}}")
        text02[0].set_color(YELLOW);text02[2].set_color(GREEN)
        text03 = TexMobject("\\therefore\,V_{\\text{黄}}","=","V_{\\text{绿}}","=","V_{\\text{红}}")
        text04 = TexMobject("\\therefore\,V_{\\text{三棱锥}}=\\frac{1}{3}Sh")

        text03[0].set_color(YELLOW);text03[2].set_color(GREEN);text03[4].set_color(ORANGE)
        text01.scale(0.5);text02.scale(0.5);text03.scale(0.5);text04.scale(0.5)
        text01.to_corner(UL),text01.shift(UP*0.1+LEFT*0.12)
        text02.next_to(text01,DOWN,aligned_edge=LEFT)
        text03.next_to(text02,DOWN,aligned_edge=LEFT)
        text04.next_to(text03,DOWN*0.8,aligned_edge=LEFT)
        self.camera.add_fixed_in_frame_mobjects(text01)
        self.camera.add_fixed_in_frame_mobjects(text02)
        self.camera.add_fixed_in_frame_mobjects(text03)
        self.camera.add_fixed_in_frame_mobjects(text04)

        texttext = TexMobject("V_{\\text{三棱锥}}=\\frac{1}{3}Sh")
        texttext.shift(DOWN*1.5+LEFT*0.165)
        self.camera.add_fixed_in_frame_mobjects(texttext)
        #3个棱锥
        facethrees1 = VGroup()
        for i in range(4):
            if(i<2):
                facethree1 = Polygon(verts1[0],verts1[i+1],verts2[0])
            if i == 2:
                facethree1= Polygon(verts1[1],verts1[2],verts2[0])    
            if i == 3:
                facethree1= Polygon(verts1[0],verts1[1],verts1[2])
            facethree1.set_stroke(width=1,color=RED)
            facethree1.set_fill(color=YELLOW,opacity=0.6)
            facethrees1.add(facethree1)
        facethrees2 = VGroup()
        for i in range(4):
            if(i<2):
                facethree2 = Polygon(verts2[0],verts2[i+1],verts1[1])
            if i == 2:
                facethree2 = Polygon(verts2[1],verts2[2],verts1[1])
            if i == 3:
                facethree2 = Polygon(verts2[0],verts2[1],verts2[2])
            facethree2.set_stroke(width=1,color=RED)
            facethree2.set_fill(color=ORANGE,opacity=0.6)
            facethrees2.add(facethree2)
        facethrees3 = VGroup()
        for i in range(4):
            if i == 0:
                facethree3 = Polygon(verts2[2],verts1[1],verts1[2])
            if i == 1:
                facethree3 = Polygon(verts1[2],verts2[0],verts2[2])
            if i == 2:
                facethree3 = Polygon(verts2[0],verts2[2],verts1[1])
            if i == 3:
                facethree3 = Polygon(verts2[0],verts1[1],verts1[2])
            facethree3.set_stroke(width=1,color=RED)
            facethree3.set_fill(color=GREEN,opacity=0.6)
            facethrees3.add(facethree3)  

        #animation
        
        self.begin_ambient_camera_rotation(rate=0.59)
        self.play(ShowCreation(face_xs[0]))
        self.play(ShowCreation(facebians_))
        self.play(ShowCreation(face_xs[1]))
        self.wait()
        self.play(ShowCreation(facethrees1))
        self.wait()
        self.play(ShowCreation(facethrees2))
        self.wait()
        self.play(ShowCreation(facethrees3))
        text04s = VGroup(text01,text02,text03,text04)
        self.play(Write(text04s[0]),Write(text04s[1]),Write(text04s[2]),Write(text04s[3]))
        self.wait(0.36)
        self.remove(face_xs[0]);self.remove(face_xs[1])
        self.remove(facebians_)
        self.play(facethrees1.shift,RIGHT*2.5)
        self.play(facethrees2.shift,(UP*math.sqrt(3)+LEFT*0.5)*2.5)
        self.play(facethrees3.shift,(DOWN*math.sqrt(3)+LEFT*0.5)*2.5)
        self.wait(3)
        self.play(facethrees1.shift,LEFT*2.5)
        self.play(facethrees2.shift,(DOWN*math.sqrt(3)+RIGHT*0.5)*2.5)
        self.play(facethrees3.shift,(UP*math.sqrt(3)+RIGHT*0.5)*2.5)
        self.wait(2.5)
        self.begin_ambient_camera_rotation(rate=-0.59)
        self.play(FadeIn(texttext))
        self.wait(6)

class lengzhui_next2(ThreeDScene):
    def construct(self):
        textleft = TexMobject("V_{\\text{三棱锥}}=\\frac{1}{3}Sh",color=RED)
        textleft.scale(0.6)
        textleft.to_edge(UL)

        textright = TextMobject("对于任意棱数大于3的棱锥\\\\","(现以五棱锥为例)\\\\",
                                "底面都可以分为若干个三角形\\\\")
        textright.scale(0.58)
        textright[1].set_color(ORANGE)
        textright.to_corner(UR)
        textright[1].shift(DOWN*0.18);textright[2].shift(DOWN*0.36)
        textright2 = TexMobject("V_{\\text{棱锥}}=\\frac{1}{3}Sh")
        textright2.scale(1)
        textright2.next_to(textright[2],DOWN*7)
        circle00 = Circle(radius=2.2)
        duo = Polygon(
            *[
                    UP*np.sin(j*2*PI/5)+RIGHT*np.cos(j*2*PI/5)
                    for j in range(5)
                ],stroke_width=2.5,stroke_color=BLUE,fill_color=BLUE
        ).scale(2.2,about_point=ORIGIN)
        vert00 = duo.get_vertices()
        xuxians = VGroup()
        for i in range(0,5,4):
            xuxian = DashedLine(vert00[2],vert00[i])
            xuxians.add(xuxian)

        textip00 = TexMobject("s_{a}","s_{b}","s_{c}")
        textip00.scale(1)
        textip00[0].move_to(xuxians[0]),textip00[0].shift(UP*0.6)
        textip00[1].move_to(xuxians[0]),textip00[1].shift(DOWN*0.68+LEFT*0.1)
        textip00[2].move_to(xuxians[1]),textip00[2].shift(DOWN*0.38+LEFT*0.38)

        textip01  = TexMobject("V_{\\text{五棱锥}}","=","V_{\\text{三棱锥}a}+V_{\\text{三棱锥}b}+V_{\\text{三棱锥}c}")
        textip02  = TexMobject("=","\\frac{1}{3}S_{a}h+\\frac{1}{3}S_{b}h+\\frac{1}{3}S_{c}h")
        textip03  = TexMobject("=","\\frac{1}{3}(S_{a}+S_{b}+S_{c})h")
        textip04  = TexMobject("=","\\frac{1}{3}Sh")
        textip01.scale(0.58);textip02.scale(0.55);textip03.scale(0.55);textip04.scale(0.55)
        textip01.next_to(textleft,2*DOWN,aligned_edge=LEFT)
        textip02.next_to(textip01[1],3.2*DOWN,submobject_to_align=textip02[0])
        textip03.next_to(textip02[0],3.2*DOWN,submobject_to_align=textip03[0])
        textip04.next_to(textip03[0],3.2*DOWN,submobject_to_align=textip04[0])
        textip04s = VGroup(textip01,textip02,textip03,textip04)
        #animation
        self.play(Write(textleft))
        self.wait()
        self.play(ShowCreation(circle00))
        self.wait()
        self.play(Write(textright[0:2],run_time = 2.5))
        self.wait(0.5)
        self.play(ShowCreation(duo))
        self.wait()
        self.play(Write(textright[2]))
        self.wait()
        self.play(ShowCreation(xuxians))
        self.wait()
        for i in range(3):
            self.play(Write(textip00[i]))
        self.wait()
        for i in range(4):
            self.play(Write(textip04s[i]));self.wait()
        self.wait(0.5)
        self.play(Write(textright2))
        self.wait(5)



class yuanzhui(ThreeDScene):
    def construct(self):
        textq = TexMobject("\\text{前置知识}3—\\text{圆锥体积推导}")
        textq.scale(1.8)
        self.play(FadeIn(textq))
        self.wait(1.6)
        self.play(FadeOut(textq))
        self.wait(0.5)
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        #self.add(axes)
        circle = Circle(radius=2)
        polys = []
        faces = []
        for i in range(3,45):
            po = Polygon(
                *[
                    UP*np.sin(j*2*PI/i)+RIGHT*np.cos(j*2*PI/i)
                    for j in range(i)
                ],stroke_width=1,stroke_color=BLUE,fill_color=BLUE,fill_opacity=0.8
            ).scale(2,about_point=ORIGIN)
            polys.append(po)
            verts = po.get_vertices()
            faces_=VGroup()    
            for j in range(i):
                if j == i-1:
                    face = Polygon(verts[j],verts[0],[0,0,3])
                else:
                    face = Polygon(verts[j],verts[j+1],[0,0,3])
                face.set_stroke(width=1,color=BLUE)
                face.set_fill(color=BLUE,opacity=0.8)
                faces_.add(face)
            faces.append(faces_)
            
        tex1 = TexMobject("\\text{棱锥体积：}\\frac{1}{3}Sh",color=RED)
        tex1.scale(0.6);tex1.to_corner(UL);tex1.shift(UP*0.1+LEFT*0.1)
        textmian = TexMobject("V_{\\text{圆锥}}=\\frac{1}{3}Sh")
        textmian2= TexMobject("V_{\\text{圆锥}}=\\frac{1}{3}\\pi{r^2}h")
        texttile = TextMobject("当棱数$n$趋向于$\\infty$时","$\\Rightarrow$","$\\ n$棱锥$=$圆锥")
        texttile.scale(0.56)
        texttile.to_edge(DOWN)
        
        texs = VGroup()
        for i in range(42):
            if(i<7):
                tex2 = TexMobject("\\text{棱数:}\,"+str(0)+str(i+3))
            
            if(i>=7):
                tex2 = TexMobject("\\text{棱数:}\,"+str(i+3))
            tex2.scale(0.8)
            tex2.to_corner(UR)
            self.camera.add_fixed_in_frame_mobjects(tex2)
            texs.add(tex2)
            
        self.camera.add_fixed_in_frame_mobjects(texs)
        self.camera.add_fixed_in_frame_mobjects(tex1)
        self.camera.add_fixed_in_frame_mobjects(textmian);self.camera.add_fixed_in_frame_mobjects(textmian2)
        self.camera.add_fixed_in_frame_mobjects(texttile)
        self.play(Write(tex1))
        self.wait()
        self.play(ShowCreation(circle))
        self.play(ShowCreation(polys[0]),ShowCreation(faces[0]),run_time=1.8)
        self.play(Write(texs[0]))
        self.wait()
        #self.begin_ambient_camera_rotation(rate=1)
        #self.wait()
        for i in range(1,10):
            self.play(
                Transform(polys[0],polys[i]),
                Transform(faces[0],faces[i]),
                Transform(texs[0],texs[i]),
                run_time=1
            )
            
        for i in range(10,22):
            self.play(
                Transform(polys[0],polys[i]),
                Transform(faces[0],faces[i]),Transform(texs[0],texs[i]),
                run_time=0.5
            )
        for i in range(22,42):
            self.play(
                Transform(polys[0],polys[i]),
                Transform(faces[0],faces[i]),Transform(texs[0],texs[i]),
                run_time=0.2
            )
        self.wait()
        self.play(Write(texttile[0]));self.play(Write(texttile[1:]))
        self.wait(1.5)
        self.play(Write(textmian))
        self.wait()
        self.play(FadeOut(textmian,run_time=1),FadeIn(textmian2,run_time=1.8))
        self.wait(5)


class qiuvs(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70 * DEGREES, theta=90 * DEGREES)
        sphere = Sphere(radius=1.5,resolution=(40,80),checkerboard_colors=[BLUE,BLUE],stroke_width=0,fill_opacity=0.7)#,
        pingmian01 = ParametricSurface(lambda u, v: [u,v,0.5],
                                    u_min=-2, u_max=2, v_min=-2, v_max=2, resolution=(100, 100),
                                    checkerboard_colors=[WHITE,WHITE],stroke_width=0)
        pingmian01.set_shade_in_3d()
        self.add(axes)
        self.add(sphere)
        self.add(pingmian01)
        self.wait(5)

class qiuvs2345(Scene):
    def construct(self):
        text001 = TextMobject("构造直径为$2R$的球，","底面直径、高为$2R$的对顶圆锥与圆柱")
        text002 = TextMobject("设球与对顶圆锥的","截面距其中心距离","为$h$")
        text002[1].set_color(YELLOW)
        text001.scale(0.5),text002.scale(0.5)
        text001.to_corner(UL)
        text002.next_to(text001,DOWN,aligned_edge=LEFT)
        text003 = TexMobject("\\text{在任意时刻有：}","S_{\\text{绿}}","+","S_{\\text{蓝}}","=","S_{\\text{红}}")
        text003[1].set_color(GREEN);text003[3].set_color("#6495FF");text003[5].set_color(RED)
        text003.scale(0.58)
        text003.shift(DOWN*1.4);text003.shift(LEFT*3)

        text004 = TexMobject("\\pi{h^2}","\\pi(R^2-h^2)","\\pi{R^2}")
        text004[0].set_color(GREEN);text004[1].set_color("#6495FF");text004[2].set_color(RED)
        text004.shift(DOWN*0.8)      
        text004.scale(0.6)
        text004[0].shift(LEFT*2.8);text004[2].shift(RIGHT*3);text004[1].shift(RIGHT*0.05)

        textlast0 = TexMobject("V_{\\text{球}}","=","V_{\\text{柱}}-V_{\\text{锥}}")
        textlast1 = TexMobject("=","2\\pi{R^3}-\\frac{2}{3}\\pi{R^3}")
        textlast2 = TexMobject("=","\\frac{4}{3}\\pi{R^3}")
        textlast0.scale(0.6);textlast1.scale(0.6);textlast2.scale(0.6)
        textlast0.shift(DOWN*1.95)
        textlast1.next_to(textlast0[1],3*DOWN,submobject_to_align=textlast1[0])
        textlast2.next_to(textlast1[0],3*DOWN,submobject_to_align=textlast2[0])
        textlasts = VGroup(textlast0,textlast1,textlast2)


        self.wait()
        self.play(Write(text001[0]),run_time=1.5);self.wait();self.play(Write(text001[1]),run_time=2.5)
        self.wait(1.5)
        self.play(Write(text002),run_time=2.5)
        self.wait()
        for i in range(3):
            self.play(Write(text004[i]))
            self.wait(0.5)
        self.wait()
        self.play(Write(text003[0]),run_time=1.5)
        self.wait()
        self.play(Write(text003[1:]),run_time=2)
        self.wait()
        for i in range(3):
            self.play(Write(textlasts[i]))
            self.wait(0.6)

class qiuvs23bmj(Scene):
    def construct(self):
        textul = TexMobject("V_{\\text{球}}=\\frac{4}{3}\\pi{R^3}",color=RED)
        textul.scale(0.5)
        textul.to_corner(UL)
        
        textx01 = TextMobject("在半径为R的球中","构造一高为$R$，","底面面积为$s$的圆锥")
        textx02 = TextMobject("将此圆锥复制$N$份，直至充满球体")
        textx03 = TextMobject("当$N$足够大，$s$足够小时")
        textxs  = VGroup(textx01,textx02,textx03)
        for i in range(3):
            textxs[i].scale(0.525)
        textx01[0].to_corner(UL);textx01[0].shift(DOWN*1.2)
        textx01[1:].next_to(textx01[0],DOWN*1.5,aligned_edge=LEFT)
        textx02.next_to(textx01[1:],DOWN*1.5,aligned_edge=LEFT)
        textx03.next_to(textx02,DOWN*1.5,aligned_edge=LEFT)

        textzmzm1 = TexMobject("V_{\\text{球}}","=","N\\times{V_{\\text{锥}}}")
        textzmzm2 = TexMobject("\\frac{4}{3}\\pi{R^3}","=","N\\times\\frac{1}{3}sR",color=RED)
        textzmzm3 = TexMobject("N\\times{s}","=","4\\pi{R^2}",color=RED)
        textzmzm4 = TexMobject("S_{\\text{球}}","=","4\\pi{R^2}",color=YELLOW)
        textzmzm2[1].set_color(WHITE);textzmzm3[1].set_color(WHITE);textzmzm4[1].set_color(WHITE)
        textzmzms = VGroup(textzmzm1,textzmzm2,textzmzm3,textzmzm4)
        textzmzm1.scale(0.7)
        for i in range(2):
            textzmzms[i+1].scale(0.63)
        textzmzm4.scale(0.75)
        textzmzm1.shift(DOWN*1.2)
        textzmzm2.next_to(textzmzm1[1],2.5*DOWN,submobject_to_align=textzmzm2[1])
        textzmzm3.next_to(textzmzm2[1],2.5*DOWN,submobject_to_align=textzmzm3[1])
        textzmzm4.next_to(textzmzm3[1],2.5*DOWN,submobject_to_align=textzmzm4[1])
        

        self.play(Write(textul))
        self.wait()
        self.play(Write(textxs[0][0]))
        self.wait()
        self.play(Write(textxs[0][1]))
        self.wait()
        self.play(Write(textxs[0][2]))
        self.wait()
        for i in range(1,3):
            self.play(Write(textxs[i]));self.wait()

        self.wait()
        for i in range(4):
            self.play(Write(textzmzms[i]));self.wait()
        self.wait()



class qiuheart(Scene):
    def construct(self):
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

class qtttt(Scene):
    def construct(self):
        q1 = TexMobject("\\text{重要极限}\\lim_{\\alpha\\rightarrow 0}\,\\frac{\\sin\\alpha}{\\alpha}=1\\text{推导}",color=BLACK)#stroke_width=4.8
        
        q1.scale(1.8)
        re = Rectangle(height = 3, width =30,stroke_width=0,fill_color = "#FF69B4",fill_opacity=0.8)
        
        self.add(re)
        self.add(q1)
        
        self.wait(5)