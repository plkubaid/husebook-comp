function un_ch(id,id2) {
  var data = document.getElementById(id);
  var data2 = document.getElementById(id2);
  data.checked = false;
  data2.checked = false;
}
function un_ch2(id) {
  var data = document.getElementById(id);
  if (data.checked) {
    data.checked = false;
  }
  else {
    data.checked = true;
  }
}

function del_pexp(id,but,sub) {
  var form = document.getElementById(id);
  alert('it will Delete it as permanent expense, click again to continue');
  form.action = "{% url 'expense:fix_cancel' %}";
  var button = document.getElementById(but);
  button.type = "hidden";
  var submit = document.getElementById(sub);
  submit.type = "submit";
}
function addRow(){
  var table = document.getElementById('inv-tab');
  var row_id = table.rows.length-2;
  var row = table.insertRow(row_id);
  row.id = 'd'+row_id;
  var pid = 'p'+row_id;
  var qid = 'q'+row_id;
  var id = 'd'+row_id;
  var cell = row.insertCell(0);
  cell.innerHTML = '<input type="text" name="code" value="" required=True >';
  var cell2 = row.insertCell(1);
  cell2.innerHTML = "<input type='number' id = '"+qid+"' name='quantity' value='1' required=True onkeyup=calc('d"+row_id+"','q"+row_id+"','p"+row_id+"');td();>";
  var cell3 = row.insertCell(2);
  cell3.innerHTML = "<input type='number' id ='p"+row_id+"' name='price' value='0' required=True onkeyup=calc('d"+row_id+"','q"+row_id+"','p"+row_id+"');td();>";
  var cell4 = row.insertCell(3);
  cell4.innerHTML = 0;
  var cell5 = row.insertCell(4);
  cell5.innerHTML = "<button type='button' name='button' onclick=deleteRow('"+id+"'); style='width:100%;' >Delete Row</button>";
}
function td() {
  var table = document.getElementById('inv-tab');
  var gt = 0;
  for (var i = 1; i < table.rows.length-2; i++) {
    gt = gt+Number(table.rows[i].cells[3].innerHTML);
  }
  var gtcell = document.getElementById('gt');
  gtcell.innerHTML = gt;
}

function calc(id,qid,pid) {
  var data = document.getElementById(id);
  var quan = document.getElementById(qid).value;
  var price = document.getElementById(pid).value;
  var total = price*quan;
  data.cells[3].innerHTML = total;
}

function deleteRow(id) {
  var data = document.getElementById(id);
  data.outerHTML="";
}
