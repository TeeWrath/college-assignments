% Get user input for sequence and N
x_original = input('Enter the discrete time sequence x[n] as a vector (e.g., [1 2 3 4]): ');
N = input('Enter the number of points for DFT (N): ');

% If sequence length is less than N, pad with zeros
if length(x_original) < N
    x_original = [x_original, zeros(1, N - length(x_original))];
elseif length(x_original) > N
    % If sequence length is greater than N, truncate the sequence
    x_original = x_original(1:N);
    disp('Warning: Sequence has been truncated to match the specified DFT length.');
end

% Display the original sequence
disp(['Original discrete-time sequence x[n]: ', num2str(x_original)]);

% Create time index for plotting
n = 0:(length(x_original)-1);

% Create the DFT matrix W
W = zeros(N, N);
for k = 0:N-1
    for n_idx = 0:N-1
        W(k+1, n_idx+1) = exp(-1j * 2 * pi * k * n_idx / N);
    end
end

% Forward DFT: X(k) = W * x(n)
X = W * x_original(:);

% Display the DFT values
disp('DFT values X(k):');
for i = 1:N
    fprintf('X(%d) = %.4f + %.4fj\n', i-1, real(X(i)), imag(X(i)));
end

% Method 1: Inverse DFT using matrix inversion
W_inv = inv(W);
x_reconstructed_inv = W_inv * X;

% Method 2: Inverse DFT using conjugate transpose (more numerically stable)
% The inverse DFT matrix is (1/N) * conjugate transpose of W
W_idft = (1/N) * W';
x_reconstructed_conj = W_idft * X;

% Calculate error between original and reconstructed signals
error_inv = norm(x_original(:) - x_reconstructed_inv);
error_conj = norm(x_original(:) - x_reconstructed_conj);

% Create a figure to compare results
figure('Position', [100, 100, 1000, 800]);

% Plot the original sequence
subplot(4, 1, 1);
stem(n, x_original, 'filled', 'LineWidth', 1.5);
grid on;
title('Original Sequence x[n]');
xlabel('n');
ylabel('Amplitude');

% Plot the DFT magnitude
subplot(4, 1, 2);
stem(n, abs(X), 'filled', 'LineWidth', 1.5);
grid on;
title('DFT Magnitude |X(k)|');
xlabel('k');
ylabel('Magnitude');

% Plot the reconstructed sequence using matrix inversion
subplot(4, 1, 3);
stem(n, real(x_reconstructed_inv), 'filled', 'LineWidth', 1.5);
grid on;
title(['Reconstructed x[n] using Matrix Inversion (Error = ', num2str(error_inv), ')']);
xlabel('n');
ylabel('Amplitude');

% Plot the reconstructed sequence using conjugate transpose
subplot(4, 1, 4);
stem(n, real(x_reconstructed_conj), 'filled', 'LineWidth', 1.5);
grid on;
title(['Reconstructed x[n] using Conjugate Transpose (Error = ', num2str(error_conj), ')']);
xlabel('n');
ylabel('Amplitude');

% Adjust the layout
sgtitle('DFT and Inverse DFT Verification using Matrix Method');

% Display the reconstructed signals
disp('Reconstructed x[n] using Matrix Inversion:');
disp(real(x_reconstructed_inv)');

disp('Reconstructed x[n] using Conjugate Transpose:');
disp(real(x_reconstructed_conj)');

% Check if the reconstruction is close to the original
if error_conj < 1e-10
    disp('Verification SUCCESSFUL: The inverse DFT recovered the original signal!');
else
    disp('Verification FAILED: The inverse DFT did not recover the original signal!');
end

% Compare numerical values
comparison_table = [n', x_original', real(x_reconstructed_inv), real(x_reconstructed_conj)];
disp('Comparison Table [n, Original x[n], IDFT_inv, IDFT_conj]:');
disp(comparison_table);
