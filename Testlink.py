from testlink import TestlinkAPIClient

def create_test_case_in_testlink(title, suite_id, project_id, content, testlink_url, devkey):
    tlc = TestlinkAPIClient(testlink_url, devkey)
    response = tlc.createTestCase(
        testcase_name=title,
        testsuiteid=suite_id,
        testprojectid=project_id,
        authorlogin='your_user',
        summary=content,
        steps='',
        expected_results=''
    )
    return response
