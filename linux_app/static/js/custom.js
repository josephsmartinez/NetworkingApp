function searchby() {
  var x = document.getElementById("mySelect").value;
  if(x == "Assest Tag"){
    document.getElementById("demo").innerHTML = `
    <form method="post">
        <div class="form-group">
    <div class="row">
      <div class="col-sm">
          <label for="exampleInputEmail1">Enter Assest Tag Number</label>
          <input type="text" class="form-control" id="tag" name="tag" aria-describedby="tag" placeholder="ATT-0000000">
        </div>
      <div class="col-sm">
        <div class="container" style="text-align:center ;padding-top:32px;">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
        </div>
    </div>
  </div>
</form>

    `;
  }
  if(x == "Mac Address"){
    document.getElementById("demo").innerHTML = `
    <form method="post">
        <div class="form-group">
    <div class="row">
      <div class="col-sm">
          <label for="exampleInputEmail1">Enter Mac Address</label>
          <input type="text" class="form-control" id="macaddr" name="macaddr" aria-describedby="macaddr" placeholder="00:00:00:00:00:00">
        </div>
      <div class="col-sm">
        <div class="container" style="text-align:center ;padding-top:32px;">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
        </div>
    </div>
  </div>
</form>

    `;
  }
  if(x == "Serial Number"){
    document.getElementById("demo").innerHTML = `
    <form method="post">
        <div class="form-group">
    <div class="row">
      <div class="col-sm">
          <label for="exampleInputEmail1">Enter Serial Number</label>
          <input type="text" class="form-control" id="macaddr" name="macaddr" aria-describedby="macaddr" placeholder="A0BC2D3E4F5">
        </div>
      <div class="col-sm">
        <div class="container" style="text-align:center ;padding-top:32px;">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
        </div>
    </div>
  </div>
</form>

    `;
  }
}