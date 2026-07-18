/*
Start
collect three subjects scores from the user
calculate the average of the three scores
if the average falls within the score scale,
it should print the letter grade associated with it.
End
**/


public class StudentGradeApplication	{
	public static void main (String[] args)	{
		java.util.Scanner input = new java.util.Scanner(System.in);
		
		System.out.println("Enter your scores for the subjects");
		System.out.println();
		
		System.out.print("Mathematics: ");
		double mathematicsScore = input.nextInt(); 

		System.out.print("English Language: ");
		double englishScore = input.nextInt();

		System.out.print("Civic Education: ");
		double civicEduScore = input.nextInt();
		
	double averageScore = (mathematicsScore + englishScore + civicEduScore) / 3 ;
		
		if(averageScore >= 90 && averageScore <= 100)	{
			System.out.println("Your Grade is: A");
		}
		if(averageScore >= 80 && averageScore < 90)	{
			System.out.println("Your Grade is: B");
		}
		if(averageScore >= 70 && averageScore < 80)	{
			System.out.println("Your Grade is: C");
		}
		if(averageScore >= 60 && averageScore < 70)	{
			System.out.println("Your Grade is: D");
		}
		if(averageScore < 60)	{
			System.out.println("Your Grade is: F");
		}
	}
}
		