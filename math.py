import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# STEP 1: Construct the Rating Matrix A (4 users x 30 movies)
# -------------------------------------------------------------
A = np.array([
    [5, 4, 5, 3, 4, 4, 5, 3, 4, 5, 1, 2, 0, 1, 2, 5, 4, 5, 4, 5, 4, 5, 3, 4, 5, 3, 4, 2, 3, 4],
    [4, 5, 3, 4, 5, 3, 2, 4, 3, 2, 5, 4, 5, 4, 5, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 2, 1, 2, 5, 4, 5, 4, 5, 0, 0, 1, 0, 1, 4, 5, 4, 5, 4, 3, 2, 4, 3, 4, 5, 4, 5, 4, 5],
    [3, 4, 5, 4, 5, 2, 3, 2, 3, 4, 0, 1, 0, 2, 0, 0, 1, 0, 0, 0, 5, 4, 5, 4, 5, 0, 0, 1, 0, 0]
], dtype=float)

# -------------------------------------------------------------
# STEP 2: Singular Value Decomposition (SVD)
# -------------------------------------------------------------
U, s, Vt = np.linalg.svd(A, full_matrices=False)

print("--- EXTRATED VALUES ---")
print(f"Singular Values (σ): {s}\n")

# -------------------------------------------------------------
# STEP 3: Plot Graphs Required by Teacher (Singular Values & Cumulative Sum)
# -------------------------------------------------------------
r_values = np.arange(1, len(s) + 1)
cumulative_variance = np.cumsum(s**2) / np.sum(s**2) * 100

fig, ax1 = plt.subplots(figsize=(8, 5))

# Plot singular values
color = 'tab:blue'
ax1.set_xlabel('Value of r (Component Index)')
ax1.set_ylabel('Singular Value Magnitude', color=color)
ax1.plot(r_values, s, marker='o', color=color, linewidth=2, label='Singular Values')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(r_values)

# Create a second y-axis sharing the same x-axis for cumulative sum
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Cumulative Variance Explained (%)', color=color)
ax2.plot(r_values, cumulative_variance, marker='s', linestyle='--', color=color, linewidth=2, label='Cumulative %')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Scree Plot: Singular Values and Cumulative Sum vs. Value of r')
fig.tight_layout()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# Print variance coverage details
for idx, var in enumerate(cumulative_variance):
    print(f"Rank-{idx+1} Truncation retains {var:.2f}% of data variance.")

# -------------------------------------------------------------
# STEP 4: Latent Mapping & User Similarity (Rank-3 Approximation)
# -------------------------------------------------------------
k = 3 # Truncate to Rank-3
U_k = U[:, :k]
s_k = np.diag(s[:k])
Vt_k = Vt[:k, :]

# Project users into 3D compressed coordinate space
user_profiles = np.dot(U_k, s_k)

# Calculate Cosine Similarity across the user Profiles
dot_product = np.dot(user_profiles, user_profiles.T)
norms = np.linalg.norm(user_profiles, axis=1, keepdims=True)
cosine_sim_matrix = dot_product / np.dot(norms, norms.T)

print("\n--- LATENT USER COSINE SIMILARITY MATRIX ---")
print(np.round(cosine_sim_matrix, 4))

# -------------------------------------------------------------
# STEP 5: Matrix Reconstruction and Imputation (Recommendation)
# -------------------------------------------------------------
A_predicted = np.dot(user_profiles, Vt_k)

print("\n--- SAMPLE PREDICTED RATINGS FOR UNWATCHED MOVIES (0s) ---")
print(f"Predicted preference for User 1 on Movie 13: {A_predicted[0, 12]:.2f}")
print(f"Predicted preference for User 2 on Movie 16: {A_predicted[1, 15]:.2f}")
print(f"Predicted preference for User 4 on Movie 16: {A_predicted[3, 15]:.2f}")