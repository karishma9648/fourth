import numpy as np
import matplotlib.pyplot as plt
subjects= ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(subjects))
performance = [10,8,6,4,2,1]
plt.grid(color='y', linestyle='--', linewidth=2, axis='y', 
alpha=0.7)
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, subjects)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()