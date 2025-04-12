import dspy

class data_parsing_agent(dspy.Signature):
    # Called to refine the query incase user query not elaborate
    """ It is your job to parse data and get rid of data defined by the user"""
    dataset = dspy.InputField(desc="Data is a .csv file with two colums named Weapon Used Cd and another that says TIME OCC ")
    Agent_desc = dspy.InputField(desc= "It is your job to restructure the data as the user requests")
    goal = dspy.InputField(desc="Eliminate all other data that is not between 1100 and 1600 or not between 2300 and 0400")
    refined_goal = dspy.OutputField(desc='It needs to be in a .csv file and it needs to originate from .csv input and it need to have two columns named Weapon Used Cd and another that says TIME OCC')
