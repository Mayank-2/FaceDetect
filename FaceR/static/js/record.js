var by_student = document.getElementById('by_student');
var by_class = document.getElementById('by_class');
var radio_student = document.getElementById('student');
var radio_class = document.getElementById('class');

// this function is use for select student attandance or class attendance 
function attendence_by() {
  if (radio_student.checked) {
    by_student.style.display = "block";
    by_class.style.display = "none";
  }
  if (radio_class.checked) {
    by_student.style.display = "none";
    by_class.style.display = "block";
  }
}


var detail_Section = document.getElementById('details');
var student_details = document.getElementById('student_details');
var class_details = document.getElementById('class_details');
function open_detail_section(num) {
  detail_Section.style.display = "flex";
  class_details.style.display = "none";
  student_details.style.display = "none";
  detail_Section.style.border = "none"
  if (num == 1) {
    student_details.style.display = "flex";
  }
  else {
    class_details.style.display = "block";
    detail_Section.style.border = "2px solid black"
  }
  event.preventDefault();
}


// ############ print ################ 

function print_details() {
  var divContents = document.getElementById("class_details").innerHTML;
  var a = window.open('', '', 'height=500, width=500');
  a.document.write('<html>');
  a.document.write('<body > <h1>Div contents are <br>');
  a.document.write(divContents);
  a.document.write('</body></html>');
  a.document.close();
  a.print();
}
