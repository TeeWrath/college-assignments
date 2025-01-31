% Question 1

x1 = input('Enter the samples of x1[n] as a vector (e.g., [1 2 3 4]): ');
n1_zero = input('Enter the position of n=0 for x1[n] (index): ');
t = input('Enter the time delay/advance (positive for delay, negative for advance): ');

n1 = (1:length(x1)) - n1_zero;

y1 = n1 - t;

figure;

subplot(2,1,1);
stem(n1, x1, 'r', 'LineWidth', 1.5); grid on;
xlabel('TIME INDEX'); ylabel('x1[n]');
title('Original Sequence x1[n]');

subplot(2,1,2);
stem(y1, x1, 'b', 'LineWidth', 1.5); grid on;
xlabel('TIME INDEX'); ylabel('y1[n]');
title(['Shifted Sequence y1[n]']);

% Question 2
x = input('Enter the samples of x[n] as a vector (e.g., [1 2 3 4]): ');
n1_zero = input('Enter the position of n=0 for x[n] (index): ');

h = input('Enter the samples of h[n] as a vector (e.g., [1 2 3 4]): ');
n2_zero = input('Enter the position of n=0 for h[n] (index): ');

n1 = (0:length(x)-1) - n1_zero;
n2 = (0:length(h)-1) - n2_zero;

n3 = (0:(length(x) + length(h) - 2)) - (n1_zero + n2_zero);
y = zeros(1, length(n3));

for i = 1:length(x)
    for j = 1:length(h)
        y(i + j - 1) = y(i + j - 1) + x(i) * h(j);
    end
end

figure;
subplot(3,1,1);
stem(n1, x, 'r', 'LineWidth', 1.5); grid on;
xlabel('TIME INDEX'); ylabel('x[n]');
title('Original Sequence x[n]');

subplot(3,1,2);
stem(n2, h, 'r', 'LineWidth', 1.5); grid on;
xlabel('TIME INDEX'); ylabel('h[n]');
title('Original Sequence h[n]');

subplot(3,1,3);
stem(n3, y, 'r', 'LineWidth', 1.5); grid on;
xlabel('TIME INDEX'); ylabel('y[n]');
title('Convoluted Sequence y[n] (Manual Calculation)');
