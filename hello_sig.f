      integer function hello_c(a)
Cf2py intent(c) hello_c
      character *(*) a
Cf2py intent(c) a
	  end

	  complex*16 function hello_f_wrap(a,z)
Cf2py intent(c) hello_f_wrap
      character *(*) a
	  complex*16 z
Cf2py intent(c) a,z
	  end
