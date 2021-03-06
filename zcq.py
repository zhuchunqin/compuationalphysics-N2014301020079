import pylab as pl
import math
class cannon_shell:
    def __init__(self,v0=700,time_step=0.5,theta=30,g=9.8,c=0.5):
        self.v0=[v0]
        self.t=[0]
        self.theta=theta*math.pi/180
        self.vx=[v0*math.cos(self.theta)]
        self.vy=[v0*math.sin(self.theta)]
        self.x=[0]
        self.y=[0]
        self.g=g
        self.dt=time_step
        self.c=c
    def calculate(self):
        _time=0
        while (self.y[-1]>=self.y[0]):
            self.vx.append(self.vx[-1])
            self.vy.append(self.vy[-1]-self.g*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(_time)
            _time +=self.dt
        r=-self.y[-2]/self.y[-1]
        self.x[-1]=(self.x[-2]+r*self.x[-1])/(r+1)
        self.y[-1]=0
    def show_results(self,color):
        pl.plot(self.x,self.y,label='theta='+str(self.theta))
        pl.title('Trajectory of cannon shell with no drag')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.xlim(0,60000)
        pl.ylim(0,20000)
        pl.legend(loc='best',prop={'size':12})
a=cannon_shell()
a.calculate()
a.show_results('r')
a=cannon_shell(v0=700,time_step=0.5,theta=35,g=9.8,c=0.5)
a.calculate()
a.show_results('r')
a=cannon_shell(v0=700,time_step=0.5,theta=40,g=9.8,c=0.5)
a.calculate()
a.show_results('r')
a=cannon_shell(v0=700,time_step=0.5,theta=45,g=9.8,c=0.5)
a.calculate()
a.show_results('r')
a=cannon_shell(v0=700,time_step=0.5,theta=50,g=9.8,c=0.5)
a.calculate()
a.show_results('r')
a=cannon_shell(v0=700,time_step=0.5,theta=55,g=9.8,c=0.5)
a.calculate()
a.show_results('r')
pl.show()
class exact_results_check(cannon_shell):
    def calculate1(self):
        _time=0
        while (self.y[-1]>=self.y[0]):
            self.vx.append(self.vx[-1])
            self.vy.append(self.vy[-1]-self.g*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(_time)
            _time +=self.dt
        r=-self.y[-2]/self.y[-1]
        self.x[-1]=(self.x[-2]+r*self.x[-1])/(r+1)
        self.y[-1]=0
    def calculate2(self):
        _time=0
        while (self.y[-1]>=self.y[0]):
            self.x.append(self.vx[0]*self.t[-1])
            self.y.append(self.vy[0]*self.t[-1]-self.c*self.g*(self.t[-1])**2)
            self.t.append(_time)
            _time +=self.dt
        r=-self.y[-2]/self.y[-1]
        self.x[-1]=(self.x[-2]+r*self.x[-1])/(r+1)
        self.y[-1]=0
    def show_results(self,color,shape):
        pl.plot(self.x,self.y,label='theta='+str(self.theta))
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.xlim(0,60000)
        pl.ylim(0,20000)
        pl.legend(loc='best',prop={'size':12})
a=exact_results_check(v0=700,time_step=0.5,theta=35,g=9.8,c=0.5)
a.calculate1()
a.show_results('r','circles')
a=exact_results_check(v0=700,time_step=0.5,theta=35,g=9.8,c=0.5)
a.calculate2()
a.show_results('r','$')
a=exact_results_check(v0=700,time_step=0.5,theta=40,g=9.8,c=0.5)
a.calculate1()
a.show_results('r','circles')
a=exact_results_check(v0=700,time_step=0.5,theta=40,g=9.8,c=0.5)
a.calculate2()
a.show_results('r','$')
a=exact_results_check(v0=700,time_step=0.5,theta=45,g=9.8,c=0.5)
a.calculate1()
a.show_results('r','circles')
a=exact_results_check(v0=700,time_step=0.5,theta=45,g=9.8,c=0.5)
a.calculate2()
a.show_results('r','$')
a=exact_results_check(v0=700,time_step=0.5,theta=50,g=9.8,c=0.5)
a.calculate1()
a.show_results('r','circles')
a=exact_results_check(v0=700,time_step=0.5,theta=50,g=9.8,c=0.5)
a.calculate2()
a.show_results('r','$')
a=exact_results_check(v0=700,time_step=0.5,theta=55,g=9.8,c=0.5)
a.calculate1()
a.show_results('r','circles')
a=exact_results_check(v0=700,time_step=0.5,theta=55,g=9.8,c=0.5)
a.calculate2()
a.show_results('r','$')
pl.show()