#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{

	vector<int> data;
	ifstream input_file;
	ofstream output_file;

	input_file.open("data.txt");

	if (input_file.is_open()) 
	{
		int val;
		while (!input_file.eof()) 
		{
			input_file >> val;
			data.push_back(val);
		}

		input_file.close();

		//insert sorting algorithm
		int i, j, key;

		for (int i = 1; i < data.size(); i++)
		{
			key = data[i]; //picking next element
			j = i - 1;

			/* Move elements of arr[0..i-1], that are 
     	   	greater than key, to one position ahead 
       		of their current position */
			while (j >= 0 && data[j] > key)
			{
				data[j + 1] = data[j];
				j = j - 1;
			}

			data[j + 1] = key;
		}

		output_file.open("insert.txt");

		for (int i = 0; i < data.size(); i++) 
		{
			output_file << data[i];
			output_file << " ";
		}

		output_file.close();
		cout << "data.txt read, values sorted and stored in insert.txt" << endl;
	}

	else 
	{
		cout << "File was not openned." << endl;
	}

	return 0;
}
