"""Generate BDA601 Assessment 2 PDF report (~1000 words)."""
from fpdf import FPDF


class Report(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def write_line(pdf, text, h=6):
    """Write wrapped text and always return cursor to left margin."""
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(pdf.epw, h, text)
    pdf.set_x(pdf.l_margin)


def add_heading(pdf, text, size=14):
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", size)
    pdf.set_text_color(20, 40, 80)
    write_line(pdf, text, h=8)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(1)


def add_para(pdf, text):
    pdf.set_font("Helvetica", "", 11)
    write_line(pdf, text, h=6)
    pdf.ln(2)


def main():
    pdf = Report()
    pdf.set_margins(18, 18, 18)
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    write_line(pdf, "BDA601 Assessment 2 Report", h=8)
    pdf.set_font("Helvetica", "B", 12)
    write_line(pdf, "Visualisation and Model Development: Telco Customer Churn", h=7)
    pdf.set_font("Helvetica", "", 11)
    pdf.ln(2)
    write_line(pdf, "Subject: BDA601 Big Data and Analytics")
    write_line(pdf, "Assessment: Individual - Source Code and Report (1,000 words +/- 10%)")
    pdf.ln(2)

    add_heading(pdf, "1. Introduction")
    add_para(
        pdf,
        "Customer churn is the movement of subscribers from one service provider to another. "
        "Retaining customers is usually cheaper than acquiring new ones, and long-term customers "
        "tend to be less costly to serve and less sensitive to competitor offers. This report "
        "supports a decision-tree churn model built from the Kaggle Telco Customer Churn "
        "IBM sample (https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data). "
        "The full extract contains 7,043 customers and 21 attributes. Per Assessment 2 Task 1, "
        "five attributes were then removed (MonthlyCharges, OnlineSecurity, StreamingTV, "
        "InternetService and Partner), leaving 16 attributes with Churn as the target. The "
        "notebook covers data extraction, exploratory analysis, cleaning, feature selection "
        "and model development. This report focuses on (a) a missing-value strategy for the "
        "most important attribute and (b) interpretation of the churn analysis outcomes."
    )

    add_heading(pdf, "2. Handling Missing Values")
    add_para(
        pdf,
        "The decision-tree model ranked Contract as the most important predictor by Gini "
        "importance (approximately 0.65), far ahead of tenure (about 0.10) and TechSupport "
        "(about 0.09). This is consistent with exploratory findings: month-to-month customers "
        "churn at about 42.7%, compared with 11.3% for one-year and 2.8% for two-year "
        "contracts. In the given dataset, Contract has no missing values. However, in real "
        "operational data a critical attribute such as Contract can be incomplete due to CRM "
        "gaps, migration errors or incomplete sign-up records."
    )
    add_para(
        pdf,
        "If a substantial share of Contract values were missing, deleting those rows would be "
        "undesirable because Contract is the dominant split feature and row deletion would "
        "shrink the training base and bias retention analysis. A practical replacement method "
        "is mode imputation within meaningful customer segments: for each incomplete record, "
        "impute Contract using the most frequent contract type among customers with similar "
        "tenure band and payment method (fallback to the global mode if a segment is too "
        "small). Contract is categorical, so the mode preserves valid category labels and "
        "avoids inventing ordinal scores. Where richer auxiliary data exist, a secondary "
        "classifier trained on complete cases could predict Contract before the main churn "
        "model; for this assessment, segmented mode imputation is transparent, reproducible "
        "and aligned with decision-tree workflows. The notebook demonstrates the impact of "
        "this idea by simulating 30% missingness in Contract and restoring values with the "
        "training-set mode, then re-fitting the tree to confirm the pipeline remains usable."
    )

    add_heading(pdf, "3. Interpretation of Churn Analysis")
    add_heading(pdf, "3.1 Effectiveness of the churn analysis", size=12)
    add_para(
        pdf,
        "On the held-out test set (20% stratified sample), the tuned decision tree "
        "(max_depth = 6, min_samples_leaf = 20, balanced class weights) achieved approximately "
        "73.2% overall accuracy and a ROC-AUC of about 0.81. In other words, the model "
        "assigned the correct churn label for roughly three-quarters of customers. Because "
        "only about 26.5% of customers churn, a trivial classifier that always predicts "
        "No would already reach about 73.5% accuracy; therefore raw accuracy alone is only "
        "borderline relative to that baseline."
    )
    add_para(
        pdf,
        "Effectiveness is more meaningful when judged by detection of actual churners. "
        "Churn recall was approximately 76% (precision about 50%), meaning the model correctly "
        "flagged about three in four customers who left, at the cost of some false alarms. "
        "For retention planning this trade-off is often acceptable: contacting a customer "
        "who would have stayed is usually cheaper than missing a high-risk customer. "
        "Overall, the analysis is a satisfactory operational starting point for targeting, "
        "provided campaigns are designed around probability scores and cost-sensitive "
        "thresholds rather than accuracy alone. It is not yet a fully optimised production "
        "model, but it is interpretable and better than chance for ranking risk (AUC about 0.81)."
    )

    add_heading(pdf, "3.2 Who is churning and what drives churn", size=12)
    add_para(
        pdf,
        "Churners are disproportionately short-tenure, flexible-contract customers. Mean "
        "tenure for churners is about 18 months versus about 38 months for retained "
        "customers. Month-to-month contracts dominate risk (42.7% churn). Payment behaviour "
        "also matters: electronic-check users churn at about 45.3%, well above automatic bank "
        "transfer (about 16.7%) and credit card (about 15.2%). Customers without TechSupport "
        "churn at about 41.6% versus about 15.2% with support. Paperless billing (about 33.6% "
        "versus 16.3%) and absence of dependents (about 31.3% versus 15.5%) further elevate "
        "risk. Collectively, the profile is a relatively new, month-to-month subscriber with "
        "limited support add-ons and a higher-friction payment method. The tree's root "
        "importance on Contract indicates that contractual lock-in is the primary structural "
        "driver; tenure and support features refine risk inside contract groups. Business "
        "drivers therefore combine switching ease (no long-term commitment), weaker product "
        "stickiness (no tech support) and billing friction - not merely demographics such as "
        "gender, which showed little importance."
    )

    add_heading(pdf, "3.3 Improving accuracy of the churn analysis", size=12)
    add_para(
        pdf,
        "Model development choices materially shaped outcomes. Cleaning blank TotalCharges "
        "values (tenure = 0 customers) by setting charges to zero prevented type errors and "
        "kept new customers in the sample. Removing customerID avoided leakage of an "
        "identifier. Stratified train/validation/test splits preserved class balance, and "
        "depth tuning on validation reduced overfitting relative to an unrestricted tree. "
        "Balanced class weights lowered pure accuracy slightly versus an unweighted tree "
        "but improved sensitivity to the minority churn class - appropriate for retention use."
    )
    add_para(
        pdf,
        "Handling missing values in Contract via informed imputation would protect the "
        "model's strongest signal; poor imputation (for example random fills) would dilute "
        "the root splits and harm both accuracy and interpretability. Accuracy and ranking "
        "quality could be improved by: (1) restoring informative removed fields where "
        "policy allows (for example MonthlyCharges, InternetService) or engineering proxies; "
        "(2) using richer encodings (one-hot or target encoding) and ensemble methods "
        "(random forest / gradient boosting) while retaining a tree for explanation; "
        "(3) calibrating thresholds with business costs instead of the default 0.5 cut-off; "
        "(4) addressing class imbalance with resampling; and (5) adding behavioural "
        "time-series features (usage drops, complaint tickets). Together, these steps should "
        "lift discrimination beyond the current AUC of about 0.81 while preserving the clear "
        "who is churning narrative required for stakeholder communication."
    )

    add_heading(pdf, "4. Conclusion")
    add_para(
        pdf,
        "A transparent decision-tree pipeline on the modified Telco dataset shows that "
        "contract type is the dominant churn signal, with tenure and support/billing "
        "attributes as secondary drivers. Test-set accuracy is about 73%, with stronger "
        "value in about 76% recall of churners and AUC near 0.81. A segmented mode-imputation "
        "strategy is recommended if Contract were heavily missing. With threshold tuning "
        "and richer features or ensembles, predictive performance can be improved without "
        "losing the interpretability that makes the analysis actionable for retention teams."
    )

    add_heading(pdf, "References")
    pdf.set_font("Helvetica", "", 10)
    write_line(
        pdf,
        "Kaggle.com. (2020). Telco customer churn - IBM sample data sets. "
        "https://www.kaggle.com/blastchar/telco-customer-churn",
        h=5,
    )

    # Word count of body paragraphs (approx)
    body = []
    for page_obj in []:
        pass
    out = "BDA601_Assessment2_Report.pdf"
    pdf.output(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    # Print word count of narrative sections
    import re
    src = open(__file__, encoding="utf-8").read()
    strings = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', src)
    # concatenate sequential short strings that look like prose in add_para - simpler count:
    text_blocks = []
    for m in re.finditer(r"add_para\(\s*pdf,\s*((?:\"[^\"]*\"\s*)+)\)", src):
        block = "".join(re.findall(r"\"([^\"]*)\"", m.group(1)))
        text_blocks.append(block)
    for m in re.finditer(r"add_heading\(pdf,\s*\"([^\"]+)\"", src):
        text_blocks.append(m.group(1))
    words = sum(len(t.split()) for t in text_blocks)
    print("Approximate report word count:", words)
    main()
