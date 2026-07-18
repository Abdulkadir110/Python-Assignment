/*
Start
Collect the father age and his son age inputs from the user.
the father age is twice as old as the son after n years.
so the father age + n years = 2(son age + n)
set the son age multiply by 2
so the twice of the son age is substracted from the father age
then the result is added to their current age to know how old they will be after n years
if the result is greater than 0, it should print it
else -1 is multiplied by the number to make it positive for the n years ago or after.
End
**/




public class FatherAndSonAge	{
	public static void main(String [] args)	{
		
		java.util.Scanner input = new java.util.Scanner(System.in);
		
		System.out.print("Enter the current age of the father's: ");
		int currentFatherAge = input.nextInt();
		
		System.out.print("Enter the current age of his son: ");
		int currentSonAge = input.nextInt();
		
		int twiceSonAge = 2 * currentSonAge;
		
		int twiceYear = currentFatherAge - twiceSonAge;
		
		int ageOfTheFather = currentFatherAge + twiceYear;
		int ageOfTheSon = currentSonAge + twiceYear;
		
		int newTwiceYear;

		if (twiceYear > 0) {
			ageOfTheFather = currentFatherAge + twiceYear;
			ageOfTheSon = currentSonAge + twiceYear;
		
	System.out.printf("The Father will be twice as old as the son after: %d years", twiceYear);	
		}
	
		if( twiceYear < 0)  {
			newTwiceYear = twiceYear * -1;
		
		System.out.printf("The Father will be twice as old as the son after: %d years", newTwiceYear);	
		}
	}
}
				
		
		