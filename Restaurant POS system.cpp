//PROJECT ON A RESTAURANT POS SYSTEM CODE 

#include<iostream>
#include<fstream>
using namespace std;
int main(){
	//VARIABLE FORMATION
	int num=0;
	int total=0;
	int quantity=0;
	int price[37]={230,330,150,170,200,250,70,130,40,230,250,150,230,180,180,180,120,40,150,150,150,90,90,90,100,120,130,130,130,80,80,80,120,120,100,60,90};
	char choice;
	int payment;
	
	
	//MENU OUTPUT
	cout<<"\t~WELCOME TO OUR RESTAURANT~\n\n\t\t~MENU~\n\n";
	cout<<"ITEM-NO\t\tITEM\t\tPRICE\n\n";
	
	
	cout<<"BURGERS:"<<endl<<"01\t\tZinger Burger\tRs."<<price[0]<<endl<<"02\t\tDouble Decker\tRs."<<price[1]<<endl;
	cout<<"03\t\tCrispy Chicken\tRs."<<price[2]<<endl<<"04\t\tChicken Tikka\tRs."<<price[3]<<endl;
	cout<<"05\t\tBBQ Burger\tRs."<<price[4]<<endl<<"06\t\tGRilled Chicken\tRs."<<price[5]<<endl<<endl;
	
	
	cout<<"PARATHAS:"<<endl<<"07\t\tPotato Paratha\tRs."<<price[6]<<endl<<"08\t\tChicken Paratha\tRs."<<price[7]<<endl;
	cout<<"09\t\tPlain Paratha\tRs."<<price[8]<<endl<<endl;
	
	
	cout<<"SANDWICHES:"<<endl<<"10\t\tGrilled Chicken\tRs."<<price[9]<<endl<<"11\t\tClub Sandwich\tRs."<<price[10]<<endl;
	cout<<"12\t\tCold Sandwich\tRs."<<price[11]<<endl<<endl;
	
	
	cout<<"ROLLS:"<<endl<<"13\t\tZinger Roll\tRs."<<price[12]<<endl<<"14\t\tTikka Roll\tRs."<<price[13]<<endl;
	cout<<"15\t\tBBQ Roll\tRs."<<price[14]<<endl<<"16\t\tCrispy Roll\tRs."<<price[15]<<endl;
	cout<<"17\t\tShawarma Roll\tRs."<<price[16]<<endl<<"18\t\tChicken Spring\tRs."<<price[17]<<endl<<endl;
	
	
	cout<<"SALADS:"<<endl<<"19\t\tFruit Salad\tRs."<<price[18]<<endl<<"20\t\tRussian Salad\tRs."<<price[19]<<endl;
	cout<<"21\t\tMacroni Salad\tRs."<<price[20]<<endl<<endl;
	
	
	cout<<"MILKSHAKES:"<<endl<<"22\t\tBanana Milkshake\tRs."<<price[21]<<endl<<"23\t\tApple Milkshake\t\tRs."<<price[22]<<endl;
	cout<<"24\t\tStrawberry Milkshake\tRs."<<price[23]<<endl<<"25\t\tMango Milkshake\t\tRs."<<price[24]<<endl;
	cout<<"26\t\tOreo Milkshake\t\tRs."<<price[25]<<endl<<"27\t\tNutella Milkshake\tRs."<<price[26]<<endl;
	cout<<"28\t\tChocolate Milkshake\tRs."<<price[27]<<endl<<"29\t\tVanilla Milkshake\tRs."<<price[28]<<endl<<endl;
	
	
	cout<<"Cold Beverages:"<<endl<<"30\t\tMint Margarita\tRs."<<price[29]<<endl<<"31\t\tLemonade\tRs."<<price[30]<<endl;
	cout<<"32\t\tPina Colada\tRs."<<price[31]<<endl<<endl;
	
	
	cout<<"Hot Beverages:"<<endl<<"33\t\tLatte\t\tRs."<<price[32]<<endl<<"34\t\tCappucino\tRs."<<price[33]<<endl;
	cout<<"35\t\tCardamom Chai\tRs."<<price[34]<<endl<<"36\t\tRegular Chai\tRs."<<price[35]<<endl;
	cout<<"37\t\tKashmiri Chai\tRs."<<price[36]<<endl<<endl;
	
	
	//looping Structure
	do{
	//MENU INPUT
	cout<<"\n\n";
	cout<<"What would you like to order?\n";
	cout<<"Enter Item-No: ";
	cin>>num;
	num=num-1;
	cout<<"Quantity: ";
	cin>>quantity;
		
	//BILL CALCULATION
	total=price[num]*quantity+total;
	
	
	//LOOP CONTINUATION
	cout<<"\n";
	cout<<"Enter '+' to order more. ";
	cin>>choice;
	
	}while(choice=='+');


	//BILL OUTPUT
	cout<<"\n\n\n\n";
	cout<<"Your Total Bill: Rs."<<total<<"/-"<<"\n\n\n";
	
	
	//PAYMENT PROCEDURE
	//INFINITE LOOP
	for(int i=1;i>0;i++){
	cout<<"Enter 1 to pay by cash and 2 to pay by card: ";
	cin>>payment;
	
	//Conditional statements
	if(payment==1){
		cout<<"\nHead to the cash counter to your left. Thankyou!";
	}
	else if(payment==2){
		cout<<"\nSwipe your card below."; //Assuming there is a card swipe machine below the pos screen
	}
	else{
		cout<<"Invalid Input\n\n";
	}
	
	//LOOP TERMINATION
	if(payment==1||payment==2){
		break;
	}
	
	}
	
	
	//FILE ADDITION
	ofstream billFile("CustomerBillHistory.txt");
	billFile<<"The previous bill was: "<<total;
	billFile.close();
	
	
	//CLOSING
	cout<<"\n\n\n"<<"\t\t\t~Enjoy your food~";
	cout<<"\n\t\t\t   (^.^)>~~*";

	return 0;
}


