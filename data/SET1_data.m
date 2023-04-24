%% SET Data Processing %%
% Mark Luke %
% 4/23/2023 %

close all
clear all
clc

%load('Burn_0.dat')
load('Burn_0.dat')

%%
time = Burn_0(:,1) - Burn_0(1,1);
fs = 1./diff(time);

%%

close all

for jj=[1:1:size(Burn_0,2)]

figure
y = Burn_0(:,jj);
plot(time, y)

end
% 8 and 10 look like tank PT curves


%%
close all
figure
t8 = Burn_0(:,8);
hold on
plot(time, t8)
xlabel('Time (s)')
ylabel('Pressure')
%% t8 looks best, normalize

t8_norm = (t8-min(t8))./(max(t8)-min(t8));
yyaxis right
plot(time, t8_norm)
ylabel('Normalized Pressure')
title('Hyperion Cold Flow Pressure Data - Column 8')
grid on

%%
X = Burn_0(:,3);
L = length(X);
Y = fft(X);
P2 = abs(Y/L);
P1 = log(P2(1:L/2+1));
P1(2:end-1) = 2*P1(2:end-1);

Fs = mean(fs);
f = Fs*(0:(L/2))/L;
figure
plot(f, P1)

%% zoom in on mdot
t8 = Burn_0(:,8);

figure
ha = fill([79.35 79.35 82.5 82.5], [100 160 160 100], [0, 0, 1]);
ha.FaceAlpha = 0.2;
hold on
plot(time, t8)
xlabel('Time (s)')
ylabel('Pressure')
xlim([78 85])


%%
figure
t10 = Burn_0(:,10);
t10_filt = lowpass(t10, 0.1);
t10_smooth = smoothdata(t10);
plot(time, t10)
hold on
plot(time, t10_filt)
plot(time, t10_smooth)

%%
t1 = Burn_0(:,5);
kulite1 = t1*221.876902 - 110.753151;

t1 = Burn_0(:,8);
omega1 = t1*200.385307 - 13.453953;

figure
hold on
plot(time, kulite1)
plot(time, omega1)