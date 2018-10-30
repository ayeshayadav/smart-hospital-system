import pymysql
class error(Exception):
    pass
class same_name(error):
    pass
db = pymysql.connect("localhost","ayeshay","ayeshay","SHS" )
cursor = db.cursor()
class patient():
    def __init__(self,username):
        self.username=username
    def view_profile(self):
        sql = ("select * from patient where username='%s'" % self.username)

        try:
            cursor.execute(sql)
            q = cursor.fetchall()
            for row in q:

                pid = row[0]

                Name = row[3]
                no = row[4]
                age = row[5]
                gender = row[6]
                depart = row[13]
                print("Your details are: ")
                print('Patient_id: ', pid, '\nName: ', Name, '\nPhone No: ', no, '\nAge: ', age, '\nGender: ', gender,
                      '\nDepartment: ', depart)
                # p=True
                # return(p)
        except:
            print("Unable to fetch data")


    def view_doctor_profile(self):
        print("""SEARCH BY:
            1.Department
            2.Doctor Id
            3.Name
            """)
        search = int(input("Enter a number from above option: "))

        if search == 1:
            dep = int(input("""Enter the department no:
                1.Physician
                2.Cardiology
                3.ENT
                4.Neurology
                5.Gynaecology
                6.Orthopaedic
                """))
            e=1
            while (e==1):
                if dep not in range(1,7):
                    print("Please enter department from above list only!")
                else:
                    e=0
            if dep==1:
                depart='physician'
            elif dep==2:
                depart='cardiology'
            elif dep==3:
                depart='ENT'
            elif dep==4:
                depart='neurology'
            elif dep==5:
                depart='gynaecology'
            elif dep==6:
                depart='orthopaedic'
            print("Available doctors are:")
            sql = ("select * from doctor where department='% s'" % (depart))
            try:
                cursor.execute(sql)
                doc = cursor.fetchall()
                for row in doc:
                    D_id = row[0]
                    Name = row[3]
                    print('DoctorID =', D_id, ', Name =', Name)
            except:
                print("Unable to fetch data")

        if search == 1 or search == 2:
            while(True):
                id = input("Enter Doctor ID: ")
                sql = ("select * from doctor where D_id='% s'" % (id))
                d=cursor.execute(sql)
                if d==0:
                    print("Enter a correct doctor ID: ")
                elif(d==1):
                    break
                    False
        elif search == 3:
            while(True):
                name = input("Enter doctors' name:")
                sql = ("select * from doctor where name = '%s'" % name)
                d=cursor.execute(sql)
                if d==0:
                    print("Enter a correct name: ")
                elif d==1:
                    break
        try:
            cursor.execute(sql)
            do = cursor.fetchall()
            for row in do:
                D_id = row[0]
                Name = row[3]
                address = row[4]
                no = row[5]
                specialisation = row[7]
                designation = row[8]
                schedule = row[10]
                charge = row[11]
                print("Doctor details are: ")
                print('Name: ', Name,'Doctor ID: ',D_id, '\nAddress: ', address, '\nPhone No: ', no, '\nSpecialisation: ', specialisation,
                      '\nDesignation: ', designation, '\nSchedule: ', schedule, '\nCharges: ', charge)

        except:
            print("Unable to fetch data")

    def book_appt(self):
        print("Available doctors for your choosen department are:")
        sql = ("select department,pid from patient where username='% s'" % (self.username))
        # sql = ("select * from doctor where department='% s'" % (dep))
        try:
            cursor.execute(sql)
            dept = cursor.fetchone()

        except:
            print("Unable to fetch data")

        sql = ("select * from doctor where department='% s'" %(dept[0]))
        try:
            cursor.execute(sql)
            doc = cursor.fetchall()
            ids=[]
            for row in doc:
                D_id = row[0]
                ids.append(D_id)
                Name = row[3]
                dsgn = row[8]
                charges = row[11]

                if dsgn== 'junior resident':
                    assign =row[0]

                print('DoctorID = ', D_id, 'Name = ', Name,'Designation = ',dsgn, 'Charges = ', charges)
        except:
            print("Unable to fetch data")

        book = input("Do you want select the doctor yourself or need help?(Y/N): ")
        if(book == 'Y' or book =='y'):

            while(True):
                s_doctor = input("Select the Doctor ID: ")
                if s_doctor in ids:
                    False
                    break
                else:
                    print("Enter correct doctor ID")

        else:
            s_doctor = assign
            print("Doctor assigned to you according to current availability is: ",s_doctor)

        date = input("Enter date in format YYYY-MM-DD : ")
        flag = (input("Do you want to confirm the appointment?(Y/N): "))

        if (flag == 'Y' or flag=='y'):
            print("Details of your appointment are: ",'\nDoctor Id: ',s_doctor,'\nDate: ',date,'\nFees: ',charges)
            order = [(dept[0],dept[1],s_doctor,date,charges)]
            sql = "insert into appointment(DEPARTMENT,PID,DID,DATE,FEES)  values(%s,%s,%s,%s,%s)"
            try:
                cursor.executemany(sql,order)
                db.commit()
            except:
                db.rollback()
        else:
            return
class doctor:
    pass
class hospital:
    pass
class department:
    pass
class admin:
    pass
class login:
    def patientlog(self):
#        self.pat = patient()
        var = True
        while (var):
            username = input("username: ")
            password = input("password: ")
            self.pat = patient(username)
            if (cursor.execute("SELECT * FROM patient where username ='" + username + "'and password='" + password + "'")):
                var = False
                db.commit()

                print("Login successful")
                p=1
                while (p):
                    print("""Choose the option:
                1. View /edit profile
                2. View doctor's profile
                3. Book appointment
                4. Make payment 
                5. Exit""")
                    op = int(input("Enter your option: "))
                    if op == 1:
                        self.pat.view_profile()

                    elif op == 2:
                        self.pat.view_doctor_profile()

                    elif op == 3:
                        self.pat.book_appt()
                    else:
                        p=0
            else:
                db.commit()
                if (cursor.execute("select * from patient where username ='" + username + "'")):
                    print("Enter valid password!")
                else:
                    print("User not registered , please register first!")
                    var = False
                    return(var)



class payment:
    def make_payment(self,name):

class critical(patient):
    pass
class non_critical(patient):
    pass

def main():
    p_login=login()
    print("WELCOME TO SMART HEALTHCARE SYSTEM!!!!!")
    ch=int(input("""Enter your choice:
    1.PATIENT
    2.DOCTOR
    3.ADMIN
    4.EXIT
    """))

    reg=False
    if ch==1:
        while(reg==False):
            a=int(input("""
    1.Login
    2.New registration
    """))
            if a==1:
                reg=p_login.patientlog()

main()