from django import forms
from.models import Mpi

class formMpi(forms.ModelForm):
    class Meta:
        model=Mpi

        fields = [

            'paciente_mpi',
            'estudio',
            's1_rest',
            's2_rest',
            's3_rest',
            's4_rest',
            's5_rest',
            's6_rest',
            's7_rest',
            's8_rest',
            's9_rest',
            's10_rest',
            's11_rest',
            's12_rest',
            's13_rest',
            's14_rest',
            's15_rest',
            's16_rest',
            's17_rest',
            's1_stress',
            's2_stress',
            's3_stress',
            's4_stress',
            's5_stress',
            's6_stress',
            's7_stress',
            's8_stress',
            's9_stress',
            's10_stress',
            's11_stress',
            's12_stress',
            's13_stress',
            's14_stress',
            's15_stress',
            's16_stress',
            's17_stress',
            's1_dif',
            's2_dif',
            's3_dif',
            's4_dif',
            's5_dif',
            's6_dif',
            's7_dif',
            's8_dif',
            's9_dif',
            's10_dif',
            's11_dif',
            's12_dif',
            's13_dif',
            's14_dif',
            's15_dif',
            's16_dif',
            's17_dif',
            'ssr',
            'sss',
            'ssd',
            'cargarchivo',
        ]

        labels = {
            'paciente_mpi':'paciente_mpi',
            'estudio':'estudio',
            's1_rest':'s1_rest',
            's2_rest':'s2_rest',
            's3_rest':'s3_rest',
            's4_rest':'s4_rest',
            's5_rest':'s5_rest',
            's6_rest':'s6_rest',
            's7_rest':'s7_rest',
            's8_rest':'s8_rest',
            's9_rest':'s9_rest',
            's10_rest':'s10_rest',
            's11_rest':'s11_rest',
            's12_rest':'s12_rest',
            's13_rest':'s13_rest',
            's14_rest':'s14_rest',
            's15_rest':'s15_rest',
            's16_rest':'s16_rest',
            's17_rest':'s17_rest',
            's1_stress':'s1_stress',
            's2_stress':'s2_stress',
            's3_stress':'s3_stress',
            's4_stress':'s4_stress',
            's5_stress':'s5_stress',
            's6_stress':'s6_stress',
            's7_stress':'s7_stress',
            's8_stress':'s8_stress',
            's9_stress':'s9_stress',
            's10_stress':'s10_stress',
            's11_stress':'s11_stress',
            's12_stress':'s12_stress',
            's13_stress':'s13_stress',
            's14_stress':'s14_stress',
            's15_stress':'s15_stress',
            's16_stress':'s16_stress',
            's17_stress':'s17_stress',
            's1_dif':'s1_dif',
            's2_dif':'s2_dif',
            's3_dif':'s3_dif',
            's4_dif':'s4_dif',
            's5_dif':'s5_dif',
            's6_dif':'s6_dif',
            's7_dif':'s7_dif',
            's8_dif':'s8_dif',
            's9_dif':'s9_dif',
            's10_dif':'s10_dif',
            's11_dif':'s11_dif',
            's12_dif':'s12_dif',
            's13_dif':'s13_dif',
            's14_dif':'s14_dif',
            's15_dif':'s15_dif',
            's16_dif':'s16_dif',
            's17_dif':'s17_dif',
            'ssr':'ssr',
            'sss':'sss',
            'ssd':'ssd',
            'cargarchivo':'cargarchivo',
        }
        widgets = {
            'paciente_mpi':forms.TextInput(attrs={'style':'margin-left: 50px; display:none;'}),
            'estudio':forms.TextInput(attrs={'style':'margin-left: 50px; display:none;'}),
            's1_rest':forms.TextInput(attrs={'id':'issr1','style':'position: absolute; left: 265px; background: transparent;top: 15px;border: 0; outline: none; height: 45px; width: 60px;text-align: center; font-size: 25px; font-weight:800;' }),
            's2_rest':forms.TextInput(attrs={'id':'issr2','style':'position: absolute; left: 265px; background: transparent;top: 70px;border: 0; outline: none; height: 45px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's3_rest':forms.TextInput(attrs={'id':'issr3' ,'style':'position: absolute; left: 112px; background: transparent;top: 122px;  border: 0; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's4_rest':forms.TextInput(attrs={'id':'issr4'  ,'style':'position: absolute; left: 160px; background: transparent;top: 138px;  border: 0; outline: none; height: 52px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's5_rest':forms.TextInput(attrs={'id':'issr5', 'style':'position: absolute; left: 265px; background: transparent;top: 125px;border: 0; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's6_rest':forms.TextInput(attrs={'id':'issr6', 'style':'position: absolute; left: 395px; background: transparent;top: 136px;border:0 ; outline: none; height: 50px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's7_rest':forms.TextInput(attrs={'id':'issr7' ,'style':'position: absolute; left: 435px; background: transparent;top: 122px;border: 0; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's8_rest':forms.TextInput(attrs={'id':'issr8' ,'style':'position: absolute; left: 200px; background: transparent;top: 180px;  border:0 ; outline: none; height: 80px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's9_rest':forms.TextInput(attrs={'id':'issr9' ,'style':'position: absolute; left: 255px; background: transparent;top: 184px;  border: 0; outline: none; height: 80px; width: 80px;text-align: center; font-size: 25px; font-weight:800;'}),
            's10_rest':forms.TextInput(attrs={'id':'issr10' ,'style':'position: absolute; left: 355px; background: transparent;top: 180px;  border: 0; outline: none; height: 80px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's11_rest':forms.TextInput(attrs={'id':'issr11' , 'style':'position: absolute; left: 112px; background: transparent;top: 280px;  border:0 ; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's12_rest':forms.TextInput(attrs={' id':'issr12' ,'style':'position: absolute; left: 160px; background: transparent;top: 260px;  border: 0; outline: none; height: 45px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's13_rest':forms.TextInput(attrs={'id':'issr13' ,'style':'position: absolute; left: 265px; background: transparent;top: 285px;  border: 0; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's14_rest':forms.TextInput(attrs={'id':'issr14' ,'style':'position: absolute; left: 385px; background: transparent;top: 260px;border:0 ; outline: none; height: 45px; width: 36px;text-align: center; font-size: 25px; font-weight:800;' ,}),
            's15_rest':forms.TextInput(attrs={'id':'issr15' ,'style':'position: absolute; left: 435px; background: transparent;top: 280px;border:0 ; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;',}),
            's16_rest':forms.TextInput(attrs={'id':'issr16' ,'style':'position: absolute; left: 265px; background: transparent;top: 335px;  border: 0; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;',}),
            's17_rest':forms.TextInput(attrs={'id':'issr17','style':'position: absolute; left: 265px; background: transparent;top: 385px;  border:0 ; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            
            's1_stress':forms.TextInput(attrs={'id':'isss1' ,'class':'par-i1','style':'position: absolute; left: 420px; background: transparent;top: 15px;border: 0; outline: none; height: 45px; width: 60px;text-align: center; font-size: 25px; font-weight:800;' }),
            's2_stress':forms.TextInput(attrs={'id':'isss2' ,'class':'par-i2' ,'style':'position: absolute; left: 420px; background: transparent;top: 70px;border: 0; outline: none; height: 45px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's3_stress':forms.TextInput(attrs={'id':'isss3' ,'class':'par-i3' ,'style':'position: absolute; left: 265px; background: transparent;top: 122px;  border: 0; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's4_stress':forms.TextInput(attrs={'id':'isss4' ,'class':'par-i4' ,'style':'position: absolute; left: 315px; background: transparent;top: 138px;  border: 0; outline: none; height: 52px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's5_stress':forms.TextInput(attrs={'id':'isss5' ,'class':'par-i5' ,'style':'position: absolute; left: 420px; background: transparent;top: 125px;border: 0; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's6_stress':forms.TextInput(attrs={'id':'isss6' ,'class':'par-i6' ,'style':'position: absolute; left: 550px; background: transparent;top: 136px;border:0 ; outline: none; height: 50px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's7_stress':forms.TextInput(attrs={'id':'isss7' ,'class':'par-i7' ,'style':'position: absolute; left: 600px; background: transparent;top: 122px;border: 0; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's8_stress':forms.TextInput(attrs={'id':'isss8' ,'class':'par-i8' ,'style':'position: absolute; left: 350px; background: transparent;top: 180px;  border:0 ; outline: none; height: 80px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's9_stress':forms.TextInput(attrs={'id':'isss9' ,'class':'par-i9' ,'style':'position: absolute; left: 410px; background: transparent;top: 184px;  border: 0; outline: none; height: 80px; width: 80px;text-align: center; font-size: 25px; font-weight:800;'}),
            's10_stress':forms.TextInput(attrs={'id':'isss10' ,'class':'par-i10' ,'style':'position: absolute; left: 510px; background: transparent;top: 180px;  border: 0; outline: none; height: 80px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's11_stress':forms.TextInput(attrs={'id':'isss11','class':'par-i11','style':'position: absolute; left: 270px; background: transparent;top: 280px;  border:0 ; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's12_stress':forms.TextInput(attrs={'id':'isss12' ,'class':'par-i12' ,'style':'position: absolute; left: 315px; background: transparent;top: 260px;  border: 0; outline: none; height: 45px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's13_stress':forms.TextInput(attrs={'id':'isss13' ,'class':'par-i13' ,'style':'position: absolute; left: 420px; background: transparent;top: 285px;  border: 0; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's14_stress':forms.TextInput(attrs={'id':'isss14' ,'class':'par-i14' ,'style':'position: absolute; left: 550px; background: transparent;top: 260px;border:0 ; outline: none; height: 45px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's15_stress':forms.TextInput(attrs={' id':'isss15' ,'class':'par-i15' ,'style':'position: absolute; left: 600px; background: transparent;top: 280px;border:0 ; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's16_stress':forms.TextInput(attrs={'id':'isss16' ,'class':'par-i16' ,'style':'position: absolute; left: 420px; background: transparent;top: 335px;  border: 0; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's17_stress':forms.TextInput(attrs={'id':'isss17', 'class':'par-i17','style':'position: absolute; left: 420px; background: transparent;top: 385px;  border:0 ; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            
            's1_dif':forms.TextInput(attrs={'id':'issd1', 'class':'par-i1', 'style':'position: absolute; left: 270px; background: transparent;top: 15px;border: 0; outline: none; height: 45px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's2_dif':forms.TextInput(attrs={'id':'issd2', 'class':'par-i2' ,'style':'position: absolute; left: 270px; background: transparent;top: 70px;border: 0; outline: none; height: 45px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's3_dif':forms.TextInput(attrs={'id':'issd3' ,'class':'par-i3' ,'style':'position: absolute; left: 120px; background: transparent;top: 122px;  border: 0; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's4_dif':forms.TextInput(attrs={'id':'issd4' ,'class':'par-i4' ,'style':'position: absolute; left: 170px; background: transparent;top: 138px;  border: 0; outline: none; height: 52px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's5_dif':forms.TextInput(attrs={'id':'issd5' ,'class':'par-i5' ,'style':'position: absolute; left: 270px; background: transparent;top: 125px;border: 0; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's6_dif':forms.TextInput(attrs={'id':'issd6' ,'class':'par-i6' ,'style':'position: absolute; left: 400px; background: transparent;top: 136px;border:0 ; outline: none; height: 50px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's7_dif':forms.TextInput(attrs={'id':'issd7' ,'class':'par-i7' ,'style':'position: absolute; left: 450px; background: transparent;top: 122px;border: 0; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's8_dif':forms.TextInput(attrs={'id':'issd8' ,'class':'par-i8' ,'style':'position: absolute; left: 200px; background: transparent;top: 180px;  border:0 ; outline: none; height: 80px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's9_dif':forms.TextInput(attrs={'id':'issd9' ,'class':'par-i9' ,'style':'position: absolute; left: 260px; background: transparent;top: 184px;  border: 0; outline: none; height: 80px; width: 80px;text-align: center; font-size: 25px; font-weight:800;'}),
            's10_dif':forms.TextInput(attrs={'id':'issd10' ,'class':'par-i10' ,'style':'position: absolute; left: 360px; background: transparent;top: 180px;  border: 0; outline: none; height: 80px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's11_dif':forms.TextInput(attrs={'id':'issd11' ,'class':'par-i11' ,'style':'position: absolute; left: 120px; background: transparent;top: 280px;  border:0 ; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's12_dif':forms.TextInput(attrs={'id':'issd12' ,'class':'par-i12' ,'style':'position: absolute; left: 170px; background: transparent;top: 260px;  border: 0; outline: none; height: 45px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's13_dif':forms.TextInput(attrs={'id':'issd13' ,'class':'par-i13' ,'style':'position: absolute; left: 270px; background: transparent;top: 285px;  border: 0; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's14_dif':forms.TextInput(attrs={'id':'issd14' ,'class':'par-i14' ,'style':'position: absolute; left: 400px; background: transparent;top: 260px;border:0 ; outline: none; height: 45px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's15_dif':forms.TextInput(attrs={'id':'issd15' ,'class':'par-i15' ,'style':'position: absolute; left: 450px; background: transparent;top: 280px;border:0 ; outline: none; height: 40px; width: 36px;text-align: center; font-size: 25px; font-weight:800;'}),
            's16_dif':forms.TextInput(attrs={'id':'issd16' ,'class':'par-i16' ,'style':'position: absolute; left: 270px; background: transparent;top: 335px;  border: 0; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            's17_dif':forms.TextInput(attrs={'id':'issd17' ,'class':'par-i17' ,'style':'position: absolute; left: 270px; background: transparent;top: 385px;  border:0 ; outline: none; height: 40px; width: 60px;text-align: center; font-size: 25px; font-weight:800;'}),
            'ssr':forms.TextInput(attrs={'id':'issr','style':'display:none'}),
            'sss':forms.TextInput(attrs={'id':'isss' ,'style':'display:none'}),
            'ssd':forms.TextInput(attrs={'id':'issd' ,'style':'display:none'}),
            'cargarchivo':forms.FileInput(attrs={'class':'form-control'}),
        }
