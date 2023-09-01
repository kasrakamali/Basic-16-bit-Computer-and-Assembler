# Basic 16-bit Computer and Assembler

This project involves designing and simulating a basic 16-bit computer in Logisim software. Additionally, an assembler is written in Python that converts assembly code to machine code, which can be used with the basic computer.

## Project Structure

The project is structured as follows:

- `Basic Computer` folder contains the files related to the basic computer circuit. To view them, open the main file named `Basic Computer.circ` using the Logisim software.
- `Assembler` folder contains the Python assembler named `Assembler.py`. To test the assembler, three assembly language programs named `source1.txt`, `source2.txt`, and `source3.txt` are placed in the same folder. By running the assembler and entering the desired source code name, its machine code is generated. Additionally, the written assembler has the ability to detect comments and can save the output file in a txt file.
- `Test Programs` folder contains three txt files for testing the designed computer circuit. To test the circuit, simply right-click on the computer memory in the Logisim software and use the Load image option to place these programs in the computer memory and then simulate it.
- `Test Results` video shows the performance of the assembler and the basic computer circuit for three different assembly language programs.

<video src="Test%20Results.mp4" controls title="Title"></video>

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.
2. Open the Logisim software and open the `Basic Computer.circ` file from the `Basic Computer` folder.
3. To test the assembler, navigate to the `Assembler` folder and run the `Assembler.py` file. Enter the desired source code name when prompted, and the machine code will be generated.
4. To test the designed computer circuit, right-click on the computer memory in the Logisim software and use the Load image option to place the program in the computer memory. Then, simulate the circuit.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

This project is based on the concepts learned from the book "Computer System Architecture" by Morris Mano.