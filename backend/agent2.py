import dspy
class data_preprocessing_agent(dspy.Signature):
    # Called to refine the query incase user query not elaborate
    """It is your job to take data and restructure it according to user defined input"""
    dataset = dspy.InputField(desc="Data based on crime in the format of a .csv file.")
    Agent_desc = dspy.InputField(desc= "It is your job to restructure the data as the user requests")
    goal = dspy.InputField(desc="Eliminate all other data that doesn't include time or type of weapon")
    refined_goal = dspy.OutputField(desc='It needs to be in a .csv file and it need to originate from .csv input and it need to have two columns named Weapon Used Cd and another that says TIME OCC')