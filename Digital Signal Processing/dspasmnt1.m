
x1 = input('Enter the samples of x1[n]: ');
n1_zero = input('Enter the position of n=0 for x1[n] (index): ');

x2 = input('Enter the samples of x2[n]: ');
n2_zero = input('Enter the position of n=0 for x2[n] (index): ');

n1 = (1:length(x1)) - n1_zero;
n2 = (1:length(x2)) - n2_zero;

n_common = min(min(n1), min(n2)) : max(max(n1), max(n2));

x1_common = zeros(1, length(n_common));
x2_common = zeros(1, length(n_common));

x1_common(ismember(n_common, n1)) = x1;

x2_common(ismember(n_common, n2)) = x2;

figure;
subplot(3, 2, 1);
stem(n1, x1, 'r', 'LineWidth', 1.5); grid on;
xlabel('n'); ylabel('x1[n]');
title('Sequence x1[n]');

subplot(3, 2, 2);
stem(n2, x2, 'b', 'LineWidth', 1.5); grid on;
xlabel('n'); ylabel('x2[n]');
title('Sequence x2[n]');

% Operations
y1 = x1_common + x2_common;
y2 = x1_common - x2_common;
y3 = x1_common .* x2_common;

% Plot y1[n]
subplot(3, 2, 3);
stem(n_common, y1, 'm', 'LineWidth', 1.5); grid on;
xlabel('n'); ylabel('y1[n]');
title('y1[n] = x1[n] + x2[n]');

% Plot y2[n]
subplot(3, 2, 4);
stem(n_common, y2, 'g', 'LineWidth', 1.5); grid on;
xlabel('n'); ylabel('y2[n]');
title('y2[n] = x1[n] - x2[n]');

% Plot y3[n]
subplot(3, 2, 5);
stem(n_common, y3, 'k', 'LineWidth', 1.5); grid on;
xlabel('n'); ylabel('y3[n]');
title('y3[n] = x1[n] .* x2[n]');
