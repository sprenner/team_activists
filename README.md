# Team Activists

You are part of the activists movement TU_hackers. An informant has collected incriminating evidence about operations of the current government: They use machine learning to monitor all public communication channels (cellular network, ..) to silence public demonstrations. Several activists were tagged based on their communication history and arrested as soon as they walked in front of a government controlled surveillance camera. 
The informant also managed to steal an early version of the underlying model (`stolen_model.pkl`). Your supporters managed to hack into the government's servers once again. Unfortunately they didn't get to download the currently used ML model, however, it was possible to set up a backdoor through which you can test your messages. (`backdoor.py`)

# Task
The `manifesto.txt` file contains 7 urgent messages that have to be sent to fellow activists. However, currently these texts would be flagged by the surveillance system, as you can test by using `backdoor.py`.
Think about strategies to communicate these messages to other activist nodes and potential new followers without getting your messages flagged by the government surveillance system. Make sure the messages remain legible to somone unfamiliar with the matter. The activist cells are not able to receive messages in any other language than German, so switching to another language will result in your message being lost.

# Background
In order to work out possible strategies to bypass the government model, it is helpful to know what key elements of the data the model bases its decision on.
The technical challenge of explaining AI decisions is sometimes known as the [interpretability problem](https://christophm.github.io/interpretable-ml-book/interpretability-importance.html).

# Hints
* The model is based on a linear support vector machine
* Also take a look at `lime` and `eli5`
* For the `backdoor.py` to work you need to fill in the `TEAMID` placeholder in the code

# Deliverables
* a `.csv` file with one column `messages` and 7 row entries containing the messages to be sent to the government model (use pandas `to_csv` function with `quoting=csv.QUOTE_ALL`)
