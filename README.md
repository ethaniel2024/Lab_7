# STAT 386 Lab 7: Data Visualization

This lab continues the cumulative STAT 386 repository. Use the cleaned General Conference talk dataset produced in the previous labs to conduct exploratory analysis and communicate one finding with a polished figure.

## Create your personal repository

1. Click **Use this template** and select **Create a new repository**.
2. For **Owner**, select `Stat386-Fall-2026`.
3. Name your repository using the format `your_netid_lab_7`.
4. Set the repository visibility to **Private**.
5. Click **Create repository**.

## Clone and set up the project

Clone your personal repository inside your `School/STAT_386` folder:

```bash
git clone <your-repository-url>
cd <your-repository-name>
uv sync
```

The first time you run `uv sync`, it will create a `uv.lock` file. Include that file in your commits.

Open the repository folder in Positron. Select the Python interpreter inside the `.venv` folder created by `uv`.

## Complete the lab

Open `lab_7.qmd` and replace `Your Name` with your name. Work through the sections in order.

Begin by loading the cleaned dataset you created in the previous lab:

`data/processed/talks_clean.csv`

You should not need to scrape the website again or modify your raw data. Lab 7 focuses on exploratory analysis and communicating findings through effective visualizations.

Complete the data-quality checks, formulate a focused exploratory question, and create at least three exploratory visualizations. Then select one visualization to develop into a polished final figure.

**Data input:** Place the cleaned talk-level dataset produced in the previous lab here as `talks_clean.csv`. Do not place raw scraped files here or overwrite the Lab 6 raw data.

**Final figure:** Save the polished final figure for Lab 7 in this directory. The Quarto document should recreate it from code when rendered.

You can preview your document with:

```bash
uv run quarto preview lab_7.qmd
```

Stop the preview by pressing `Ctrl+C` in the terminal. Make several meaningful commits as you work. For example:

```bash
git add lab_7.qmd scripts/visualize_data.py
git commit -m "Complete exploratory visualizations"
git push
```

## Work with the AI Collaborator

After completing your exploratory analysis and polished final figure, commit and push your work. You will then review two proposed changes to your visualization code. Each interaction creates a Pull Request.

Both reviews ask you to evaluate a visualization choice and determine whether it communicates the data accurately. Inspect the proposed code, consider its effect on interpretation, and decide whether the change is appropriate.

You are evaluated on your reasoning and ability to improve visual communication, not simply on whether you accept or reject the proposed change.

### First AI Collaborator interaction

Create a new Issue using the **Lab 7 Complete** Issue template. If the template is unavailable, create a regular Issue titled `Lab 7 complete`; its description can be empty.

Post the following command as a **new comment**, not in the Issue description:

```text
@local-llm-user process config-dir: Lab_7/metadata_01.yml in instructor-repo: Stat386-Fall-2026/Instructor_Repo
```

Once the collaborator creates a Pull Request:

1. Read the Pull Request description.
2. Inspect the proposed code in **Files changed**.
3. Answer every review question in a comment on that Pull Request.
4. Explain whether the proposed addition fits the lab and communicates the data accurately.
5. Merge the Pull Request if appropriate, or close the Pull Request without merging if inappropriate.

You are evaluated on your reasoning, not on accepting the change. You do not need to execute a proposed visualization simply to evaluate its design.

If you merge the Pull Request, update your local repository before continuing:

```bash
git pull
```

### Second AI Collaborator interaction

After reviewing the first Pull Request, return to the **same Lab 7 completion Issue**. If the Issue was closed automatically, reopen it before posting the next command.

Post the following command as a new comment:

```text
@local-llm-user process config-dir: Lab_7/metadata_02.yml in instructor-repo: Stat386-Fall-2026/Instructor_Repo
```

Review the second Pull Request using the same process. Answer all questions in a comment and explain your decision to merge or close it. If you merge it, run `git pull` again.

## Render and submit

After both reviews, render the final document from a fresh session:

```bash
uv run quarto render lab_7.qmd
```

Commit and push your completed document, rendered HTML, visualization script, dependency lockfile, cleaned dataset, and final figure:

```bash
git add lab_7.qmd lab_7.html scripts/visualize_data.py uv.lock data/processed/talks_clean.csv figures/
git commit -m "Complete Lab 7"
git push
```

Follow the submission directions provided in Canvas.

## Deliverables

- Completed `lab_7.qmd`.
- At least three exploratory visualizations.
- One polished final figure saved in `figures/`.
- A concise interpretation and discussion of limitations.
- A response to both AI visualization reviews.

This is exploratory analysis. Describe patterns; do not make causal claims or present visual comparisons as formal statistical inference.
