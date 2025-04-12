clc; clear; close all;
wp = 0.4 * pi;
ws = 0.6 * pi;
A = -3;
As = 60;
wc = (wp + ws) / 2;
trans_bw = (ws - wp) / (2*pi);

N = ceil((As - 8) / (2.285 * (ws - wp)));
N = max(N, 1);
N = N + mod(N+1, 2);
Len = N;
n = 0:Len;
alpha = Len / 2;
hd = zeros(size(n));
for i = 1:length(n)
   if (n(i) == alpha)
       hd(i) = wc / pi;
   else
       hd(i) = sin(wc * (n(i) - alpha)) / (pi * (n(i) - alpha));
   end
end

hamm_window = zeros(size(n));
for i = 1:length(n)
   hamm_window(i) = 0.54 - 0.46 * cos(2 * pi * n(i) / Len);
end

h = hd .* hamm_window;
Nfft = 1024;
omega = linspace(0, pi, Nfft);
wp_index = round(0.4 * Nfft / pi);
Htemp = 0;
for m = 1:length(h)
   Htemp = Htemp + h(m) * exp(-1j * omega(wp_index) * (m - 1));
end

gain_at_wp = abs(Htemp);
desired_gain = 10^(A/20);
h = h * (desired_gain / gain_at_wp);
H = zeros(1, Nfft);
for k = 1:Nfft
   for m = 1:length(h)
       H(k) = H(k) + h(m) * exp(-1j * omega(k) * (m - 1));
   end
end
figure;
plot(omega/pi, 20*log10(abs(H)), 'LineWidth', 1.5);
xlabel('Normalized Frequency (\times\pi rad/sample)');
ylabel('Magnitude (dB)');
title('Magnitude Response');
grid on;
ylim([-100 5]);
figure;
plot(omega/pi, unwrap(angle(H)), 'LineWidth', 1.5);
xlabel('Normalized Frequency (\times\pi rad/sample)');
ylabel('Phase (radians)');
title('Phase Response (Manual)');
grid on;
fprintf('Filter Order (N): %d\n', Len);
disp('Filter Coefficients h[n]:');
disp(h);
