const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

// Define the MotelCustomer object
const MotelCustomer = {
  name: "Buddy Wassisname"
  ,birthDate: new Date("1981-01-01")
  ,gender: "Non-binary"
  ,roomPreferences: ["pet-friendly", "view of the pool"]
  ,Pet: "goldfish"
  ,paymentMethod: ["rare coins", "Mastercard"]
  ,mailingAddress: {
    street: "123 Main St"
    ,city: "Anytown"
    ,province: "NL"
    ,postalCode: "A1A 1A1"
    ,country: "CAN"
  }
  ,phoneNumber: "(709) 555-1234"
  ,checkInOut: {
    checkInDate: new Date("2024-07-20")
    ,checkOutDate: new Date("2024-07-25")
  }
  // Method to calculate age
  ,getAge: function() {
    const today = new Date();
    let age = today.getFullYear() - this.birthDate.getFullYear();
    const month = today.getMonth() - this.birthDate.getMonth();
    if (month < 0 || (m === 0 && today.getDate() < this.birthDate.getDate())) {
      age--;
    }
    return age;
  }
  // Method to calculate duration of stay
  ,getDurationOfStay: function() {
    const msDuration = this.checkInOut.checkOutDate - this.checkInOut.checkInDate;
    const duration = msDuration / (1000 * 60 * 60 * 24);
    return duration;
  }

  // Method to create a description of the customer
  ,getDescription: function() {
    return `
  <p>Customer Name: ${this.name}</br>
  </br>
  Age: ${this.getAge()}</br>
  Gender: ${this.gender}</br>
  Room Preferences: ${this.roomPreferences.join(", ")}</br>
  Payment Method: ${this.paymentMethod.join(", ")}</br>
  Mailing Address: ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.province}, ${this.mailingAddress.postalCode}, ${this.mailingAddress.country}</br>
  Phone Number: ${this.phoneNumber}</br>
  Check-in Date: ${this.checkInOut.checkInDate.toDateString()}</br>
  Check-out Date: ${this.checkInOut.checkOutDate.toDateString()}</br>
  Duration of Stay: ${this.getDurationOfStay()} days<\p>
    `;
  }
};


// For fun, here is a motel customer class so we can create multiple customers

class MotelGuest {
  constructor(firstName, lastName, birthDate, gender, roomPreferences, pet, paymentMethod, mailingAddress, phoneNumber, checkInDate, checkOutDate) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.birthDate = new Date(birthDate);
    this.gender = gender;
    this.roomPreferences = roomPreferences;
    this.pet = pet;
    this.paymentMethod = paymentMethod;
    this.mailingAddress = mailingAddress;
    this.phoneNumber = phoneNumber;
    this.checkInOut = {
      checkInDate: new Date(checkInDate),
      checkOutDate: new Date(checkOutDate)
    };
  }

  // Method to calculate the age
  getAge() {
    const today = new Date();
    let age = today.getFullYear() - this.birthDate.getFullYear();
    const currentYearBirthday = new Date(today.getFullYear(), this.birthDate.getMonth(), this.birthDate.getDate());
    if (today < currentYearBirthday) {
      age--;
    }
    return age;
  }

  getFormatedBirhDate() {
    // Format the date
    const date = new Date(this.birthDate.getFullYear(), this.birthDate.getMonth(), this.birthDate.getDate());
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const formattedDate = `${months[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}`;
    
    return formattedDate;
    }
  

  // Method to calculate the duration of stay
  getDurationOfStay() {
    const timeDiff = this.checkInOut.checkOutDate - this.checkInOut.checkInDate;
    const duration = timeDiff / (1000 * 60 * 60 * 24); // Convert milliseconds to days
    return duration;
  }

  getMailingAddress() {
    const { street, city, prov, postalCode, country } = this.mailingAddress;
    const formattedAddress = `${street}, ${city}, ${prov}, ${postalCode}, ${country}`;
    return formattedAddress;
  }

  // Methods to create a description of the customer
  getSillyAnecdote() {
    return `
      <p><h4>Story 1, with guest ${this.firstName} ${this.lastName}:</h4> <\p>
      <p>"Hey, you remember that guest, <b>${this.firstName} ${this.lastName}</b> in room 210? Let me tell you, they've been quite the character. Born on <b>${this.getFormatedBirhDate()}</b>, making them <b>${this.getAge()}</b>, but they act like they're 20. First, they checked in on <b>${this.checkInOut.checkInDate.toDateString()}</b> and managed to lock themself out of their room within the first hour! Then, they asked for a <b>${this.roomPreferences[0]}</b> room with a <b>${this.roomPreferences[1]}</b>, turns out this was for their pet <b>${this.pet}</b>! The next morning, they called the front desk to ask if we could arrange a surprise birthday party for their pet, complete with balloons and a small cake. And if that wasn’t enough, they tried to pay their bill with a <b>${this.paymentMethod[1]}</b>. I had to politely explain we only accept credit cards, so they finally handed over their <b>${this.paymentMethod[0]}</b>. I even heard they once tried to ride the luggage cart down the hallway! We’ve had some strange requests, but <b>${this.firstName}</b> definitely takes the cake. Oh, and if you need to call them for anything, their number is <b>${this.phoneNumber}</b>. Just be prepared for anything!"<\p>
     `;}

  getNiceAnecdote() {
    return `
      <p><h4>Story 2, with guest ${this.firstName} ${this.lastName}:</h4> <\p>
      <p>"Have you heard about <b>${this.firstName} ${this.lastName}</b> in room 502? She’s probably one of the best customers we’ve ever had. Born on <b>${this.getFormatedBirhDate()}</b>, she’s <b>${this.getAge()}</b> and just the sweetest person. <b>${this.firstName}</b> checked in on <b>${this.checkInOut.checkInDate.toDateString()}</b> and will be staying with us for <b>${this.getDurationOfStay()}</b> days. She booked a suite with a <b>${this.roomPreferences[0]}</b>, <b>${this.roomPreferences[1]}</b>, of course. Every morning she leaves a small thank you note and a generous tip for housekeeping. She paid with her <b>${this.paymentMethod[0]}</b> and even took the time to compliment the front desk staff for their helpfulness. Her mailing address is <b>${this.getMailingAddress()}</b>, if you ever want to send her a thank you card. And get this – she even brought in homemade cookies for the staff yesterday! If you ever need to reach her, her phone number is <b>${this.phoneNumber}</b>. <b>${this.firstName}</b> has been an absolute pleasure, and we’ll definitely miss her when she checks out on the <b>${this.checkInOut.checkOutDate.getDate()}</b>th."<\p>
  `;}
}


// Creating instances for two customers
const guest1 = new MotelGuest(
  "Buddy"
  ,"Wassisname"
  ,"1981-01-01"
  ,"Non-binary"
  ,["pet-friendly", "view of the pool"]
  ,"goldfish"
  ,["Mastercard", "collection of rare coins"]
  ,{ street: "123 Main St", city: "Anytown", prov: "NL", postalCode: "A1A 1A1", country: "CAN" }
  ,"(709) 555-1234"
  ,"2024-07-20"
  ,"2024-07-25"
);

const guest2 = new MotelGuest(
  "Missus"
  ,"Wassername"
  ,"1970-10-10"
  ,"Female"
  ,["non-smoking", "ocean view"]
  ,"rock"
  ,["VISA", "IOU"]
  ,{ street: "123 Side St", city: "Othertown", prov: "NL", postalCode: "A2B 3C4", country: "CAN" }
  ,"(709) 555-5678"
  ,"2023-08-01"
  ,"2023-08-05"
);


// Log the description of the MotelCustomer
console.log("MotelCustomer Description:");
console.log("");
console.log(MotelCustomer.getDescription());


// Log the descriptions of both guests from the MotelGuest class
console.log("Staff gossip from Motel Guest Classes:");
console.log("");
console.log(guest1.getSillyAnecdote());
console.log(guest2.getNiceAnecdote());


// Display the MotelCustomer description in the HTML
document.getElementById('customer-info').innerHTML = MotelCustomer.getDescription();
document.getElementById('guest-info').innerHTML += guest1.getSillyAnecdote();
document.getElementById('guest-info').innerHTML += guest2.getNiceAnecdote();

document.getElementById('guest-info2').innerHTML += guest2.getSillyAnecdote();
document.getElementById('guest-info2').innerHTML += guest1.getNiceAnecdote();


