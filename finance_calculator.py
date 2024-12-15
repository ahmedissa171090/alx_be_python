m_incom = int (input ( " Enter your monthly income:"))
m_expenses =int ( input ("Enter your total monthly expenses:"))
monthly_savings = m_incom - m_expenses
print("Your monthly savings are" , monthly_savings)
Projected_Savings =monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is:" , Projected_Savings)