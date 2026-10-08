from pathlib import Path
import unittest


class TestLoanReport(unittest.TestCase):
	"""Ensure the loan report model contains a usable SQL query."""

	@classmethod
	def setUpClass(cls):
		project_root = Path(__file__).resolve().parents[1]
		cls.report_files = list(project_root.rglob("loan_report.sql"))

	def test_loan_report_model_exists(self):
		self.assertTrue(self.report_files, "Expected to find a loan_report.sql model")

	def test_loan_report_model_is_file(self):
		self.assertTrue(all(path.is_file() for path in self.report_files))

	def test_loan_report_is_readable(self):
		for path in self.report_files:
			with self.subTest(path=path):
				self.assertIsInstance(path.read_text(encoding="utf-8"), str)

	def test_loan_report_query_is_non_empty(self):
		for path in self.report_files:
			with self.subTest(path=path):
				self.assertTrue(path.read_text(encoding="utf-8").strip())

	def test_loan_report_query_contains_select(self):
		for path in self.report_files:
			with self.subTest(path=path):
				self.assertIn("select", path.read_text(encoding="utf-8").lower())

	def test_loan_report_query_has_sql_extension(self):
		self.assertTrue(all(path.suffix == ".sql" for path in self.report_files))
