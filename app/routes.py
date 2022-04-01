from dis import dis
from inspect import _void
from flask import render_template, flash, Blueprint, request
from .BMI_calc import BMI

view = Blueprint('view', __name__)

@view.route('/', methods=['GET', 'POST'])
def index():
	# Display bmi is an indicator to the html to either display the bmi or not (if calculated)
	display_bmi = False
	bmi = 0
	if request.method == 'POST':
		feet = request.form.get("feet")
		inches = request.form.get("inches")
		weight = request.form.get("weight")
		if feet == '':
			feet = 0
		if weight == '':
			weight = 0
		if inches == '':
			inches = 0
			
		bmi = BMI(float(feet), float(inches), float(weight))
		display_bmi = True

	return render_template('home.html', display_bmi=display_bmi, bmi=bmi)
