# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

---

## Dataset

Data set is from CMU Movie Summary Corpus. Data is already downloaded into the 
repository, however link to dataset can be found **here**: 
https://www.cs.cmu.edu/~ark/personas/

## Setup

### Uses Python3
#### Create the virtual environment
1. Open your terminal in the project directory and run:
      `python -m venv venv`
This creates a new directory named venv that contains an isolated Python environment.
2. Activate the virtual environment

   On macOS/Linux, run: 

         source venv/bin/activate

   On Windows, run:

         venv\Scripts\activate

   When activated, your terminal prompt should change to show the name of the virtual environment.

3. Install project dependencies

   With the virtual environment activated, install the required packages by running:

         pip install -r requirements.txt

4. Deactivate the virtual environment

   When you’re finished working, simply run:

         deactivate

## Running Code

If using VScode or any ide, simply click `Run Python File`

If on terminal, naivgate to project directory and run:

      python reccomender.py

Then once the prompt `Query:` appears, enter a query and press enter.

## Results

```console
>>python recommender.py
Query:
I want to watch a sci-fi film

       title                                                      plot
1      The Bridge  Sea Org officer Ronnie Miscavige describes the planetary Scientology dissemination campaign. Aft...
2   Ab Insaf Hoga  The film deals with a woman's  fight against corruption. She has always a strong support in her ...
3  From the Drain  The film is centered on two men in a bathtub; it is implied that they are veterans of some past ...
4          Vixen!  In the heart of the Canadian wilderness, sultry and sexually assertive Vixen becomes quickly bor...
5      1 a Minute  The film is a hybrid between narrative structure and documentary style set to interweave through...

Salary expectation: $5000/month
```