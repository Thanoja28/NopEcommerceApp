from datetime import datetime

from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

            ### pytest HTML Report ###

# Hook for adding Environment info for HTML Report


# @pytest.hookimpl(optionalhook=True)
# def pytest_html_results_summary(prefix, summary, postfix):
#     html_block = """
#         <div style="font-size:14px; margin-top:10px;">
#             <p><b>Project:</b> NopCommerce</p>
#             <p><b>Browser:</b> Chrome</p>
#             <p><b>Environment:</b> QA</p>
#             <p><b>Tester:</b> Thanoja</p>
#         </div>
#     """
#     prefix.append(html_block)



#Table format

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    html_block = """
        <table style="width:50%; border-collapse: collapse; margin-top: 15px; font-size: 14px;">
            <tr style="background-color:#f2f2f2;">
                <th style="border:1px solid #ddd; padding:8px; text-align:left;">Field</th>
                <th style="border:1px solid #ddd; padding:8px; text-align:left;">Details</th>
            </tr>
            <tr>
                <td style="border:1px solid #ddd; padding:8px;">Project</td>
                <td style="border:1px solid #ddd; padding:8px;">NopCommerce</td>
            </tr>
            <tr>
                <td style="border:1px solid #ddd; padding:8px;">Browser</td>
                <td style="border:1px solid #ddd; padding:8px;">Chrome</td>
            </tr>
            <tr>
                <td style="border:1px solid #ddd; padding:8px;">Environment</td>
                <td style="border:1px solid #ddd; padding:8px;">QA</td>
            </tr>
            <tr>
                <td style="border:1px solid #ddd; padding:8px;">Tester</td>
                <td style="border:1px solid #ddd; padding:8px;">Thanoja</td>
            </tr>
        </table>
    """
    prefix.append(html_block)


