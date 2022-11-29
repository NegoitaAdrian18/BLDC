"""
Acest script a fost preluat din matlab si va fi prelucrat cu ajutorul Python
""""""

"""



# n=9
# power_of_2 =2^n; % 2^10  =  1024
# signal = Magnetic_torque; %
# signal(end:power_of_2)=0; % Am adaugat 0 la sfarsitul vectorului pana la 1024 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Trq =Magnetic_torque;
#
# t = ANGPOS_ROTOR;
# t(end:power_of_2)=0; % Am adaugat 0 la sfarsitul vectorului pana la 1024  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# time = ANGPOS_ROTOR;
# x=1:power_of_2; %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
# % Array indexing
# t1 = t(1,1); % Am accesat primul element din array
# t2 = t(1,2); % Am accesat al doilea element din array
# dt = t2-t1;
#
# fs = 1/dt;
# Y = fft(signal);  % FFT on Tr signal
# f_fft = x.*(fs/power_of_2);%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
# z = 2/(power_of_2);  %%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
# A = z.*abs(Y); % Amplitude
#
#
# pp = 12; % numarul de poli
# dinte = 27;  %numarul de dinti de pe stator
#
# P_mp = 360/pp; % Perioada unghiulara a magnetilor permanenti >>> Pas unghiular
# P_dinte = 360/dinte;  % Perioada unghiulara a dintilor
# lcmm = lcm(dinte, pp); % cel mai mic multipu comun dintre numarul de dinti statorici si numarul de magneti permanenti
# f_mp = 1/P_mp; % ???? frecventa magentilor permanenti intalnita in fft ?????
# f_dintr = 1/dinte; % ???? frecventa dintinlor intalnita in fft ??????
#
#
# figure(1)
# plot(f_fft, A);
# xlabel('f_fft')
# ylabel('A')
# grid on
#
# figure(2)
# plot(time, Trq)
# xlabel('Time [s]')
# ylabel('Tr  [Nm]')