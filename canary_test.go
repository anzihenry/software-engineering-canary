package canary

import "testing"

func TestSynthetic(t *testing.T) {
	if !Synthetic() {
		t.Fatal("canary must remain synthetic")
	}
}
