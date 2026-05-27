# EvoLife Simulation 🧬🎮

An AI-based evolution simulation built using Python, Pygame, and Neural Networks.  
In this project, virtual creatures learn to survive by finding food, conserving energy, and evolving better movement behavior over generations using mutation and natural selection.

---

## 📌 Features

- 🧠 Simple Neural Network controlled creatures
- 🍏 Food-seeking survival mechanism
- ⚡ Energy-based life system
- 🧬 Genetic evolution with mutation
- 📈 Fitness-based natural selection
- 🎨 Real-time simulation using Pygame
- 🔄 Automatic generation evolution

---

## 🛠️ Technologies Used

- Python 3
- Pygame
- NumPy
- Math & Random libraries

---

## 📂 Project Structure

```bash
EvoLife-Simulation/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🚀 How It Works

### 1. Creature Initialization
Each creature is created with:
- Random starting position
- Energy level
- Neural Network brain
- Movement speed

### 2. Neural Network Decision Making
The neural network receives:
- Distance direction to nearest food
- Bias input

It then decides:
- X-axis movement
- Y-axis movement

### 3. Food Consumption
When creatures touch food:
- Energy increases
- Fitness score increases
- New food is spawned

### 4. Evolution Process
When all creatures die (or a creature reaches high fitness):
- Best creatures are selected as parents
- Their neural networks are copied
- Mutation creates new behaviors
- New generation starts

---

## 🧠 Neural Network

The project uses a very simple feed-forward neural network:

- **Inputs:** 3
- **Outputs:** 2
- **Activation Function:** tanh()

The weights mutate over generations to improve survival behavior.

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/EvoLife-Simulation.git
cd EvoLife-Simulation
```

### Step 2: Install Dependencies

```bash
pip install pygame numpy
```

OR

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| Close Window | Exit Simulation |

---

## 📊 Simulation Statistics

The simulation displays:
- Current Generation
- Alive Creatures
- Best Fitness in Current Generation
- Best Fitness of All Time

---

## 🔮 Future Improvements

- Add obstacle avoidance
- Predator-prey ecosystem
- Advanced neural networks
- Save/load trained generations
- Graph visualization of evolution
- Genetic crossover system

---

## 📸 Preview

You can add screenshots or GIFs here after uploading the project to GitHub.

Example:

```md
![Simulation Screenshot](images/demo.png)
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

Developed by **Shreya Pol**
