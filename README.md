# An attempt to predict the need for mental therapy of employee by given a survey that aims to measure attitudes towards mental health in the tech workplace, and examine the frequency of mental health disorders among tech workers.

## The final result: A model that can predict with high probability if The patient needs mental therapy.

For more details and pictures:
http://www.morc.io/Machine%20Learning%20Mental%20health%20prediction

I've got a bunch of data so I had to do some preprocessing data before (Inculded in the git repo).

The data content:

-Timestamp

-Age

-Gender

-Country

-state: If you live in the United States, which state or territory do you live in?

-self_employed: Are you self-employed?

-family_history: Do you have a family history of mental illness?

-treatment: Have you sought treatment for a mental health condition?

-work_interfere: If you have a mental health condition, do you feel that it interferes with your work?

-no_employees: How many employees does your company or organization have?

-remote_work: Do you work remotely (outside of an office) at least 50% of the time?

-tech_company: Is your employer primarily a tech company/organization?

-benefits: Does your employer provide mental health benefits?

-care_options: Do you know the options for mental health care your employer provides?

-wellness_program: Has your employer ever discussed mental health as part of an employee wellness program?

-seek_help: Does your employer provide resources to learn more about mental health issues and how to seek help?

-anonymity: Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?

-leave: How easy is it for you to take medical leave for a mental health condition?

-mental_health_consequence: Do you think that discussing a mental health issue with your employer would have negative consequences?

-phys_health_consequence: Do you think that discussing a physical health issue with your employer would have negative consequences?

-coworkers: Would you be willing to discuss a mental health issue with your coworkers?

-supervisor: Would you be willing to discuss a mental health issue with your direct supervisor(s)?

-mental_health_interview: Would you bring up a mental health issue with a potential employer in an interview?

-phys_health_interview: Would you bring up a physical health issue with a potential employer in an interview?

-mental_vs_physical: Do you feel that your employer takes mental health as seriously as physical health?

-obs_consequence: Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?

-comments: Any additional notes or comments

After that I tested a few algorithms:

1. Random Forest.

2. Logistic Regression.

3. SVM.

4. AdaptiveBoost

5. XGBoost.

The final result is Random Forest algorithm producing the best accurecy.

So I have a model that can produce a diagnosis according to the data in database with 83.14% accurecy :)
