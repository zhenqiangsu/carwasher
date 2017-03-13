from flask import Flask, render_template, request, flash
from carwasher.forms import ContactForm
app = Flask(__name__)
import carwasher.views
