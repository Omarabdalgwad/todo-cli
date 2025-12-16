"""
Tests for position validation in todo-cli.
Tests that invalid positions are handled gracefully with helpful error messages.
"""

import os
import pytest
from typer.testing import CliRunner
from todocli.todo import app
from todocli import database


@pytest.fixture(autouse=True)
def clean_database():
    """Clean up the database before and after each test."""
    # Clear all todos from the database
    database.c.execute("DELETE FROM todos")
    database.conn.commit()
    yield
    # Clean up after test
    database.c.execute("DELETE FROM todos")
    database.conn.commit()


@pytest.fixture
def runner():
    """Create a CLI runner for testing."""
    return CliRunner()


class TestDeleteValidation:
    """Tests for delete command position validation."""

    def test_delete_empty_database(self, runner):
        """Test deleting from empty database shows helpful error."""
        result = runner.invoke(app, ["delete", "1"])
        assert result.exit_code == 1
        assert "No todos exist" in result.output

    def test_delete_position_too_high(self, runner):
        """Test deleting with position higher than total todos."""
        runner.invoke(app, ["add", "Test task", "study"])
        result = runner.invoke(app, ["delete", "100"])
        assert result.exit_code == 1
        assert "Position 100 does not exist" in result.output
        assert "Valid positions are 1 to 1" in result.output

    def test_delete_position_zero(self, runner):
        """Test deleting with position 0 shows error."""
        runner.invoke(app, ["add", "Test task", "study"])
        result = runner.invoke(app, ["delete", "0"])
        assert result.exit_code == 1
        assert "positive number" in result.output

    def test_delete_valid_position(self, runner):
        """Test deleting with valid position succeeds."""
        runner.invoke(app, ["add", "Test task", "study"])
        result = runner.invoke(app, ["delete", "1"])
        assert result.exit_code == 0


class TestUpdateValidation:
    """Tests for update command position validation."""

    def test_update_empty_database(self, runner):
        """Test updating in empty database shows helpful error."""
        result = runner.invoke(app, ["update", "1", "--task", "New task"])
        assert result.exit_code == 1
        assert "No todos exist" in result.output

    def test_update_position_too_high(self, runner):
        """Test updating with position higher than total todos."""
        runner.invoke(app, ["add", "Test task", "study"])
        result = runner.invoke(app, ["update", "50", "--task", "New task"])
        assert result.exit_code == 1
        assert "Position 50 does not exist" in result.output

    def test_update_position_zero(self, runner):
        """Test updating with position 0 shows error."""
        runner.invoke(app, ["add", "Test task", "study"])
        result = runner.invoke(app, ["update", "0", "--task", "New task"])
        assert result.exit_code == 1
        assert "positive number" in result.output

    def test_update_valid_position(self, runner):
        """Test updating with valid position succeeds."""
        runner.invoke(app, ["add", "Test task", "study"])
        result = runner.invoke(app, ["update", "1", "--task", "Updated task"])
        assert result.exit_code == 0


class TestCompleteValidation:
    """Tests for complete command position validation."""

    def test_complete_empty_database(self, runner):
        """Test completing in empty database shows helpful error."""
        result = runner.invoke(app, ["complete", "1"])
        assert result.exit_code == 1
        assert "No todos exist" in result.output

    def test_complete_position_too_high(self, runner):
        """Test completing with position higher than total todos."""
        runner.invoke(app, ["add", "Test task", "study"])
        result = runner.invoke(app, ["complete", "25"])
        assert result.exit_code == 1
        assert "Position 25 does not exist" in result.output

    def test_complete_position_zero(self, runner):
        """Test completing with position 0 shows error."""
        runner.invoke(app, ["add", "Test task", "study"])
        result = runner.invoke(app, ["complete", "0"])
        assert result.exit_code == 1
        assert "positive number" in result.output

    def test_complete_valid_position(self, runner):
        """Test completing with valid position succeeds."""
        runner.invoke(app, ["add", "Test task", "study"])
        result = runner.invoke(app, ["complete", "1"])
        assert result.exit_code == 0


class TestDatabaseHelpers:
    """Tests for database helper functions."""

    def test_get_todo_count_empty(self):
        """Test get_todo_count returns 0 for empty database."""
        assert database.get_todo_count() == 0

    def test_get_todo_count_with_todos(self, runner):
        """Test get_todo_count returns correct count."""
        runner.invoke(app, ["add", "Task 1", "study"])
        runner.invoke(app, ["add", "Task 2", "work"])
        assert database.get_todo_count() == 2

    def test_is_valid_position_empty_database(self):
        """Test is_valid_position returns False for empty database."""
        assert database.is_valid_position(0) is False
        assert database.is_valid_position(1) is False

    def test_is_valid_position_negative(self, runner):
        """Test is_valid_position returns False for negative position."""
        runner.invoke(app, ["add", "Task", "study"])
        assert database.is_valid_position(-1) is False

    def test_is_valid_position_valid(self, runner):
        """Test is_valid_position returns True for valid position."""
        runner.invoke(app, ["add", "Task", "study"])
        assert database.is_valid_position(0) is True  # 0-indexed

    def test_is_valid_position_too_high(self, runner):
        """Test is_valid_position returns False for position >= count."""
        runner.invoke(app, ["add", "Task", "study"])
        assert database.is_valid_position(1) is False  # 0-indexed, only 0 is valid


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
